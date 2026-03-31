# 📊 Data Science Pipeline

End-to-end data pipeline built in Python with a production-ready mindset.

---

## 🚀 Overview

This project implements a complete data pipeline, covering the full lifecycle:

* Data ingestion from CSV
* Data validation (schema + quality checks)
* Data transformation (Polars)
* Aggregation and feature engineering
* SQL-based analytics (DuckDB)
* Machine learning training (LightGBM)
* Logging, retry logic, and CLI execution

The project is designed to simulate a real-world **data engineering + DevOps workflow**.

---

## 🧱 Project Structure

```
src/
├── data/        # Pipeline (ingestion, transformation, SQL)
├── models/      # Machine learning training
├── utils/       # Logger, validation, retry logic
├── jobs/        # Job runner (execution layer)

tests/           # Unit tests (pytest)
data/            # Raw + processed data (ignored in git)
.github/         # CI/CD workflows
```

---

## ⚙️ Tech Stack

* Python
* Polars (data processing)
* DuckDB (SQL analytics)
* Scikit-learn / LightGBM (ML)
* Pytest (testing)
* Poetry (dependency management)
* GitHub Actions (CI/CD)
* Black & Flake8 (code quality)
* Pre-commit hooks (local automation)

---

## ▶️ How to Run

### Install dependencies

```
poetry install
```

---

### Run pipeline

```
poetry run python -m src.data.pipeline --input data/raw/sales.csv --min-total 100
```

---

### Run job runner

```
poetry run python -m src.jobs.run_pipeline
```

---

### Run tests

```
poetry run pytest
```

---

## 🔁 CI/CD

The project uses GitHub Actions to automatically:

* Install dependencies
* Run formatter (Black)
* Run lint checks (Flake8)
* Execute unit tests
* Run the data pipeline

Every push and pull request is validated automatically.

---

## 🧪 Testing

* Unit tests implemented with pytest
* Covers:

  * Data transformation
  * Data validation

Includes both:

* Positive cases
* Error scenarios

---

## 🧹 Code Quality

* Black → automatic formatting
* Flake8 → linting and best practices
* Pre-commit hooks → checks before every commit

Ensures consistent and clean code across the project.

---

## 🧠 Key Features

* Modular architecture (`src/`)
* CLI-based pipeline execution
* Retry logic for robustness
* Data validation layer
* SQL analytics with DuckDB
* CI/CD integration
* Automated testing
* Code quality enforcement

---

## 📌 Future Improvements

* Docker containerization
* Kubernetes job execution
* Data versioning
* Feature store integration
* Monitoring & observability (metrics/logs)
* Kafka ingestion (streaming pipeline)

---

## 👨‍💻 Author

Andrea Di Francesco

---

## ⭐ Notes

This project is designed to simulate a real production-ready pipeline,
combining data engineering, machine learning, and DevOps practices.
