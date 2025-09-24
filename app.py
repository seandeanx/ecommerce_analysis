import os
import sys
import pandas as pd


def main():
    print("Packages loaded successfully ✅")

    data_path = os.path.join(os.path.dirname(__file__), 'sales_transaction.csv')

    if not os.path.exists(data_path):
        print(f"Data file not found at: {data_path}")
        print("Files in project dir:")
        for f in os.listdir(os.path.dirname(__file__)):
            print(' -', f)
        sys.exit(1)

    try:
        df = pd.read_csv(data_path)
    except Exception as e:
        print('Error reading CSV:', e)
        sys.exit(1)

    print(f'Loaded data with shape: {df.shape}')
    print('Columns:', list(df.columns))
    print('First 5 rows:')
    print(df.head().to_string(index=False))


if __name__ == '__main__':
    main()
