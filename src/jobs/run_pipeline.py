import subprocess
import sys
import logging
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("runner")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw/sales.csv")
    parser.add_argument("--min-total", default="200")
    return parser.parse_args()


def run_pipeline():
    args = parse_args()

    cmd = [
        "poetry",
        "run",
        "python",
        "-m",
        "src.data.pipeline",
        "--input",
        args.input,
        "--min-total",
        str(args.min_total),
    ]

    try:
        logger.info("Starting pipeline job...")

        result = subprocess.run(cmd, check=True)

        logger.info("Pipeline completed successfully")

        return result.returncode

    except subprocess.CalledProcessError as e:
        logger.error(f"Pipeline failed with exit code {e.returncode}")
        sys.exit(e.returncode)


if __name__ == "__main__":
    run_pipeline()
