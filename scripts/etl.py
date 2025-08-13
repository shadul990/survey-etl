import pandas as pd
import argparse
from pathlib import Path

def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    if 'value' in df.columns:
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
    return df

def main(input_path: str, output_path: str):
    input_path = Path(input_path)
    output_path = Path(output_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    df = pd.read_csv(input_path)
    df_clean = clean(df)
    if 'id' in df_clean.columns:
        df_clean = df_clean.dropna(subset=['id'])
    df_clean.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple ETL script")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output", required=True, help="Path to output cleaned CSV")
    args = parser.parse_args()
    main(args.input, args.output)
