# Data Science Pipeline Project

## Overview
End-to-end data pipeline with:
- Data ingestion (Polars)
- Transformation
- Storage (Parquet)
- Analytics (DuckDB)
- Machine Learning

## Tech Stack
- Python
- Poetry
- Polars
- DuckDB
- Scikit-learn / LightGBM

## How to run

### Install dependencies
poetry install

### Run pipeline
poetry run python src/data/pipeline.py

### Train model
poetry run python src/models/train.py

## Project Structure

ds-project/
├── data/
├── src/
│   ├── data/
│   ├── models/
├── config/
├── logs/
├── tests/


## Architecture

Raw Data → Polars → Transformation → Parquet → DuckDB → ML Model

## Purpose

This project aims to simulate a real-world data pipeline integrating data engineering and machine learning workflows.