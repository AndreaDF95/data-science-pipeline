import polars as pl
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from lightgbm import LGBMRegressor
# import shap


def explain_model(model, X):
    # explainer = shap.Explainer(model)
    # shap_values = explainer(X)

    print("SHAP values calculated")


def load_data(path: str) -> pl.DataFrame:
    return pl.read_parquet(path)


# def prepare_features(df: pl.DataFrame):
#    # target
#    y = df["total_amount"]

# features (senza target)
#    X = df.drop("total_amount")


#    return X.to_pandas(), y.to_pandas()
def prepare_features(df: pl.DataFrame):
    df = df.with_columns(
        [(pl.col("total_amount") / pl.col("num_transactions")).alias("avg_ticket")]
    )

    df = df.select(["avg_amount", "num_transactions", "avg_ticket", "total_amount"])

    y = df["total_amount"]
    X = df.drop("total_amount")

    return X.to_pandas(), y.to_pandas()


# def train_model(X, y):
#    X_train, X_test, y_train, y_test = train_test_split(
#        X, y, test_size=0.2, random_state=42
#    )

#    model = RandomForestRegressor()
#    model.fit(X_train, y_train)

#    preds = model.predict(X_test)

#    mse = mean_squared_error(y_test, preds)

#    print(f"MSE: {mse}")

#    return model


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LGBMRegressor()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    mse = mean_squared_error(y_test, preds)

    print(f"MSE: {mse}")

    return model


if __name__ == "__main__":
    df = load_data("data/processed/sales.parquet")

    X, y = prepare_features(df)

    model = train_model(X, y)

    explain_model(model, X)
