#!/usr/bin/env python3
"""
Auto-download Telecom Customer Churn dataset from Kaggle
Requires: pip install kaggle

Usage:
    python download_dataset.py
"""

import os
import subprocess
import sys
from pathlib import Path

def download_dataset():
    """Download dataset from Kaggle API"""

    # Check if Kaggle CLI is installed
    try:
        import kaggle
    except ImportError:
        print("❌ Kaggle CLI not found!")
        print("\nInstall with: pip install kaggle")
        print("Then configure: kaggle config set -n api_key -v YOUR_API_KEY")
        sys.exit(1)

    # Create data directory
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    print("📥 Downloading Telecom Customer Churn dataset...")

    try:
        # Download dataset
        subprocess.run(
            ["kaggle", "datasets", "download", "-d", "blastchar/telco-customer-churn", "-p", str(data_dir)],
            check=True
        )

        # Unzip
        zip_file = data_dir / "telco-customer-churn.zip"
        if zip_file.exists():
            print("📦 Extracting files...")
            subprocess.run(
                ["unzip", "-o", str(zip_file), "-d", str(data_dir)],
                check=True
            )
            zip_file.unlink()  # Remove zip after extraction

        print("✅ Dataset downloaded successfully!")
        print(f"📁 Location: {data_dir.absolute()}")

        # List files
        csv_files = list(data_dir.glob("*.csv"))
        print(f"\n📋 CSV files in data/:")
        for f in csv_files:
            print(f"   - {f.name}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Error downloading dataset: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_dataset()
