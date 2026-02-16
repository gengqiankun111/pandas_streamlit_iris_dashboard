# data_processing.py
import pandas as pd
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

def load_and_preprocess_iris_data():
    IRIS_CSV_URL = os.getenv("DATA_URL")
    try:
        # 1. Read online CSV data
        df = pd.read_csv(IRIS_CSV_URL)

        # 2. Data inspection: missing values, duplicate values
        missing_values = df.isnull().sum()
        duplicate_rows = df.duplicated().sum()

        # 3. Data cleaning: remove duplicate values
        if duplicate_rows > 0:
            df = df.drop_duplicates()

        # 4. Optional: reset index (index becomes discontinuous after removing duplicates)
        df = df.reset_index(drop=True)

        return df, missing_values, duplicate_rows

    except Exception as e:
        # Catch all possible exceptions (network issues, data format issues, etc.)
        raise Exception(f"Data processing failed: {str(e)}")


# Test function (optional, verify functionality when running this file)
if __name__ == "__main__":
    try:
        df, missing, duplicate = load_and_preprocess_iris_data()
        print("Data loaded successfully!")
        print(f"Data dimensions: {df.shape}")
        print(f"Missing values statistics:\n{missing}")
        print(f"Number of duplicate values: {duplicate}")
    except Exception as e:
        print(e)