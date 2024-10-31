import yfinance as yf
import pandas as pd
from db_utils import save_to_db  # Import the function from db_utils

def collect_data(tickers, start_date, end_date):
    """Fetch historical price data for given tickers from Yahoo Finance."""
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

if __name__ == "__main__":
    # Define parameters for data collection
    tickers = 'AAPL'  # Example ticker, can be a string or list of tickers
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    
    # Collect data from Yahoo Finance
    raw_data = collect_data(tickers, start_date, end_date)
    
    # Save raw data to the database
    save_to_db(raw_data)
    print("Data collection and saving to database completed.")
