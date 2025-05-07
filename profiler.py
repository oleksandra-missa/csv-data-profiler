import pandas as pd
import sys

def profile_csv(file_path):
    print(f"Dataset: {file_path}")
    print("-" * 40)
    
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"Shape: {df.shape}\n")

    for col in df.columns:
        print(f"Column: {col}")
        print(f" - Type: {df[col].dtype}")
        print(f" - Missing: {df[col].isna().sum()}")
        
        if pd.api.types.is_numeric_dtype(df[col]):
            print(f" - Mean: {df[col].mean():.2f}")
            print(f" - Median: {df[col].median():.2f}")
            print(f" - Std: {df[col].std():.2f}")
            print(f" - Min: {df[col].min()}")
            print(f" - Max: {df[col].max()}")
        elif pd.api.types.is_string_dtype(df[col]):
            print(f" - Unique Values: {df[col].nunique()}")
        
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python profiler.py <path_to_csv>")
    else:
        profile_csv(sys.argv[1])
