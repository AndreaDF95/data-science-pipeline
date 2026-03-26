import polars as pl
import duckdb
import os
from src.utils.logger import get_logger
from src.utils.validation import validate_dataframe
from src.utils.retry import retry

logger = get_logger()


@retry(max_attempts=3, delay=2)
def load_data(path: str):
    logger.info(f"Loading data from {path}")
    df = pl.read_csv(path)

    logger.info("Validating data")
    validate_dataframe(df)

    return df


def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    logger.info("Transforming data")
    return (
        df
        .with_columns([
            pl.col("amount").cast(pl.Float64),
            pl.col("date").str.to_date()
        ])
        .group_by("customer_id")
        .agg([
            pl.col("amount").sum().alias("total_amount"),
            pl.col("amount").mean().alias("avg_amount"),
            #pl.count().alias("num_transactions") -- deprecated in favor of len()
            pl.len().alias("num_transactions")
        ])
    )

    

def save_data(df, path: str):
    logger.info(f"Saving data to {path}")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.write_parquet(path)


def run_sql_analysis(parquet_path: str):
    query = f"""
        SELECT
            customer_id,
            total_amount,
            avg_amount
        FROM read_parquet('{parquet_path}')
        WHERE total_amount > 200
    """
    return duckdb.sql(query).df()


if __name__ == "__main__":
    df = load_data("data/raw/sales.csv")
    df_transformed = transform_data(df)

    save_data(df_transformed, "data/processed/sales.parquet")

    result = run_sql_analysis("data/processed/sales.parquet")

    print(result)