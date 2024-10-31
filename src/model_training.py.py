import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib  # For saving the model

def load_feature_data(db_name="data/database.sqlite"):
    """Load feature data from the database."""
    conn = sqlite3.connect(db_name)
    query = "SELECT * FROM asset_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def train_model(data):
    """Train a Random Forest model on the feature data."""
    # Define the features and target variable
    X = data.drop(columns=['Close'])  # Adjust target as needed
    y = data['Close']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")

    return model

def save_model(model, filename='model.joblib'):
    """Save the trained model to a file."""
    joblib.dump(model, filename)

if __name__ == "__main__":
    # Load feature data
    feature_data = load_feature_data()

    # Train the model
    trained_model = train_model(feature_data)

    # Save the trained model
    save_model(trained_model)
