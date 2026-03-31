import polars as pl
from src.data.pipeline import transform_data


def test_transform_basic():
    df = pl.DataFrame(
        {
            "customer_id": [1, 1, 2],
            "amount": [100, 200, 300],
            "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        }
    )

    result = transform_data(df)

    # controlli base
    assert result.shape[0] == 2
    assert "total_amount" in result.columns
    assert "avg_amount" in result.columns
