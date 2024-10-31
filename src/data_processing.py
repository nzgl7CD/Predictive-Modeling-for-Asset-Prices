import pandas as pd
from db_utils import save_to_db  # Import the function from db_utils
import sqlite3

def clean_data(data):
    """Cleans the data by filling missing values and dropping any remaining NaNs."""
    data = data.fillna(method='ffill').dropna()
    return data

def view_database(db_name="data/database.sqlite"):
    """Fetches data from the database."""
    conn = sqlite3.connect(db_name)
    query = "SELECT * FROM asset_data"  # Adjust this if the table is not created yet
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    # Fetch raw data from the database
    raw_data = view_database()  # This should already have data saved by data_collection.py

    # Clean the raw data
    cleaned_data = clean_data(raw_data)

    # Save the cleaned data back to the database
    save_to_db(cleaned_data)  # Save cleaned data to the database
