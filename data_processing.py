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
        df.to_csv("iris_data_sample.csv", index = False)

        # 2. Data inspection: check for missing values and duplicate records
        missing_values = df.isnull().sum()
        duplicate_rows = df.duplicated().sum()

        # 3. Handle missing values: remove rows with null values if any exist
        # Check if there are any missing values in the dataset
        total_missing = missing_values.sum()
        if total_missing > 0:
            # Remove rows containing null values
            df = df.dropna()
            print(f"Removed {total_missing} missing values from the dataset")

        # 4. Data cleaning: remove duplicate values
        if duplicate_rows > 0:
            df = df.drop_duplicates()
            print(f"Removed {duplicate_rows} duplicate rows from the dataset")

        # 5. Reset index after data cleaning operations
        # Index becomes discontinuous after removing rows, so we reset it
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