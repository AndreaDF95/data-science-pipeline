Write-Host "Starting pipeline..."

poetry run python -m src.data.pipeline --input data/raw/sales.csv --min-total 200

if ($LASTEXITCODE -eq 0) {
    Write-Host "Pipeline completed successfully"
} else {
    Write-Host "Pipeline failed"
    exit 1
}