import pandas as pd
from db_utils import save_to_db  # Import the save_to_db function from db_utils
import sqlite3


def load_cleaned_data(db_name="data/database.sqlite"):
    """Load cleaned data from the database."""
    conn = sqlite3.connect(db_name)
    query = "SELECT * FROM asset_data" 
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def create_features(data):
    """Create features from the cleaned data."""
    # Example: Calculate Simple Moving Average (SMA)
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    
    # Example: Calculate Exponential Moving Average (EMA)
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()

    # Example: Calculate Relative Strength Index (RSI)
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    
    # Add more features as needed...
    
    return data

def save_features_to_db(data, db_name="data/database.sqlite"):
    """Save the new features back to the database using db_utils."""
    save_to_db(data, db_name)  

if __name__ == "__main__":
    # Load cleaned data
    cleaned_data = load_cleaned_data()

    # Create features
    featured_data = create_features(cleaned_data)

    # Save featured data to the database
    save_features_to_db(featured_data)
