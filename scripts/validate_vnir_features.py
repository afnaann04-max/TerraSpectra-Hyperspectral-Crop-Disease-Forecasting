
"""
Validate a processed VNIR feature dataset.

Checks:
1. Dataset dimensions
2. Missing values
3. Duplicate rows
4. Constant columns
5. Numeric feature statistics
6. Highly correlated feature pairs

The script reports potential issues but does not modify
or delete the original dataset.
"""

import argparse
from pathlib import Path

import pandas as pd


def validate_dataset(input_file, output_dir):
    input_path = Path(input_file)
    output_path = Path(output_dir)

    if not input_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {input_path}"
        )

    output_path.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path)

    print("\n===== VNIR DATASET VALIDATION =====")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    # Missing values
    missing = df.isnull().sum()
    missing_report = missing[missing > 0].reset_index()
    missing_report.columns = ["Column", "Missing_Count"]
    missing_report.to_csv(
        output_path / "missing_values_report.csv",
        index=False
    )

    # Duplicate rows
    duplicate_count = int(df.duplicated().sum())

    # Constant columns
    constant_columns = [
        column for column in df.columns
        if df[column].nunique(dropna=False) <= 1
    ]

    # Numeric feature statistics
    numeric_df = df.select_dtypes(include="number")
    statistics = numeric_df.describe().T
    statistics.to_csv(
        output_path / "feature_statistics.csv"
    )

    # Highly correlated numeric feature pairs
    correlation = numeric_df.corr()
    correlation_pairs = []

    columns = correlation.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            value = correlation.iloc[i, j]

            if pd.notna(value) and abs(value) >= 0.98:
                correlation_pairs.append({
                    "Feature_1": columns[i],
                    "Feature_2": columns[j],
                    "Correlation": value
                })

    correlation_report = pd.DataFrame(
        correlation_pairs,
        columns=["Feature_1", "Feature_2", "Correlation"]
    )

    correlation_report.to_csv(
        output_path / "high_correlation_pairs.csv",
        index=False
    )

    print(f"\nDuplicate rows: {duplicate_count}")
    print(f"Columns with missing values: {len(missing_report)}")
    print(f"Constant columns: {constant_columns}")
    print(f"Highly correlated pairs: {len(correlation_pairs)}")

    print(f"\nReports saved in: {output_path.resolve()}")
    print("\nValidation completed.")


def main():
    parser = argparse.ArgumentParser(
        description="Validate a processed VNIR feature CSV."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the processed VNIR CSV file."
    )

    parser.add_argument(
        "--output",
        default="reports/vnir_validation",
        help="Folder for validation reports."
    )

    args = parser.parse_args()

    validate_dataset(args.input, args.output)


if __name__ == "__main__":
    main()
