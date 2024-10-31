import sqlite3

def save_to_db(data, table_name='asset_data', db_name="data/database.sqlite"):
    """
    Save DataFrame to SQLite database.
    
    Parameters:
    - data (DataFrame): DataFrame containing asset data.
    - table_name (str): Name of the table to save the data into.
    - db_name (str): Path to the SQLite database.
    """
    conn = sqlite3.connect(db_name)
    data.to_sql(table_name, conn, if_exists='replace', index=True)  # Use 'replace' for overwriting
    conn.close()
