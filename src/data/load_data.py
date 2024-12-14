import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Preprocess the data.
    
    Args:
    df (pd.DataFrame): Raw data.
    
    Returns:
    pd.DataFrame: Preprocessed data.
    """
    # ...existing code...
    # Add preprocessing steps here
    # ...existing code...
    return df
