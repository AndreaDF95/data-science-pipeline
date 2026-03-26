import polars as pl


def validate_dataframe(df: pl.DataFrame):
    if df.is_empty():
        raise ValueError("DataFrame is empty")

    required_columns = ["customer_id", "amount", "date"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    if df["amount"].null_count() > 0:
        raise ValueError("Column 'amount' contains null values")

    return True