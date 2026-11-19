"""Shared utilities for bronze layer notebooks: save raw files, delta tables, and integrity logs.

PragatiGati: India National Infrastructure & PM Gati Shakti Monitoring.
"""

import datetime
import hashlib
import json
import os

from src import config

# Indian Standard Time (IST) is UTC+05:30
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

LOG_COLUMNS = (
    "run_id string, source string, table_name string, rows_expected long, rows_loaded long, "
    "raw_copy string, source_url string, "
    "raw_files array<struct<path: string, size_bytes: long, sha256: string>>"
)


def new_run_id() -> str:
    """A new ID for an ingestion run, e.g. 20261118T120000123456+0530.

    Generates time in IST (Indian Standard Time) so runs are chronologically orderable.
    """
    return datetime.datetime.now(IST).strftime("%Y%m%dT%H%M%S%f+0530")


def landing_folder(*parts: str) -> str:
    """Create a folder in the landing volume or local landing directory and return its path."""
    path = os.path.join(config.LANDING, *parts).replace("\\", "/")
    os.makedirs(path, exist_ok=True)
    return path


def save_raw(path: str, content: bytes) -> tuple:
    """Save an API reply or source file exactly as received.

    Returns (path, size_bytes, sha256_hash) for cryptographic integrity audit.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(content)
    return path, len(content), hashlib.sha256(content).hexdigest()


def raw_file(path: str) -> tuple:
    """Compute (path, size_bytes, sha256_hash) for an existing file."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            digest.update(block)
    return path, os.path.getsize(path), digest.hexdigest()


def write_json_lines(path: str, records: list) -> None:
    """Save records as JSON Lines (NDJSON). Spark or pandas can read directly."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(
            json.dumps(record, ensure_ascii=False) + "\n" for record in records
        )


def table_name(table: str, schema: str = config.BRONZE) -> str:
    """Full table identifier with backticks for Databricks Lakehouse SQL."""
    return f"`{config.CATALOG}`.`{schema}`.{table}"


def save_table(spark, df, table: str, run_id: str, schema: str = config.BRONZE):
    """Replace Delta table with current run's rows, plus metadata columns. Safe to re-run."""
    from pyspark.sql import functions as F

    df_stamped = df.withColumn("_ingest_run_id", F.lit(run_id)).withColumn(
        "load_ts", F.current_timestamp()
    )
    full_table = table_name(table, schema)
    df_stamped.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable(
        full_table
    )
    return spark.table(full_table).count()


def log_load(
    spark,
    run_id: str,
    source: str,
    table: str,
    rows_expected: int,
    rows_loaded: int,
    raw_files: list,
    source_url: str,
):
    """Logs ingestion telemetry into 01-bronze.load_log for provenance and data lineage."""
    from pyspark.sql import functions as F

    paths = [path for path, _, _ in raw_files]
    raw_copy = paths[0] if len(paths) == 1 else os.path.commonpath(paths)
    row = [
        (
            run_id,
            source,
            table,
            int(rows_expected),
            int(rows_loaded),
            raw_copy,
            source_url,
            [(path, size, sha256) for path, size, sha256 in raw_files],
        )
    ]
    log = spark.createDataFrame(row, LOG_COLUMNS).withColumn(
        "load_ts", F.current_timestamp()
    )
    log.write.mode("append").option("mergeSchema", "true").saveAsTable(
        table_name("load_log")
    )
