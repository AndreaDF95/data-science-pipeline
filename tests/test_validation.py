import polars as pl
import pytest
from src.utils.validation import validate_dataframe


def test_validation_ok():
    df = pl.DataFrame({
        "customer_id": [1],
        "amount": [100],
        "date": ["2024-01-01"]
    })

    assert validate_dataframe(df) is True


def test_validation_missing_column():
    df = pl.DataFrame({
        "customer_id": [1],
        "date": ["2024-01-01"]
    })

    with pytest.raises(ValueError):
        validate_dataframe(df)