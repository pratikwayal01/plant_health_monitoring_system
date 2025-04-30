"""
Data processing utilities for the Plant Health Monitoring System
"""
import pandas as pd
from datetime import datetime


def process_csv_data(df):
    """
    Process the CSV data for analysis and visualization
    
    Args:
        df (pd.DataFrame): DataFrame containing sensor data
        
    Returns:
        dict: Processed data with time series for each parameter
    """
    # Ensure correct data types
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    numeric_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'pH', 'rainfall']
    
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Drop rows with NaN values
    df = df.dropna()
    
    # Sort by timestamp
    df = df.sort_values('timestamp')
    
    # Format timestamps for Chart.js
    df['formatted_timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d')
    
    # Calculate average, min, max for each parameter
    stats = {
        'averages': {},
        'min': {},
        'max': {}
    }
    
    for col in numeric_columns:
        stats['averages'][col] = round(df[col].mean(), 2)
        stats['min'][col] = round(df[col].min(), 2)
        stats['max'][col] = round(df[col].max(), 2)
    
    # Prepare data for Chart.js
    chart_data = {}
    for col in numeric_columns:
        chart_data[col] = {
            'labels': df['formatted_timestamp'].tolist(),
            'values': df[col].tolist()
        }
    
    # Calculate trend direction (increasing, decreasing, stable)
    trends = {}
    for col in numeric_columns:
        if len(df) >= 2:
            first_half = df[col].iloc[:len(df)//2].mean()
            second_half = df[col].iloc[len(df)//2:].mean()
            
            if second_half > first_half * 1.05:  # 5% increase
                trends[col] = "increasing"
            elif second_half < first_half * 0.95:  # 5% decrease
                trends[col] = "decreasing"
            else:
                trends[col] = "stable"
        else:
            trends[col] = "insufficient_data"
    
    # Prepare final result
    result = {
        'chart_data': chart_data,
        'stats': stats,
        'trends': trends,
        'latest_values': {col: float(df[col].iloc[-1]) for col in numeric_columns}
    }
    
    return result


def validate_csv_format(file):
    """
    Validate that the CSV file has the required format
    
    Args:
        file: The uploaded file object
        
    Returns:
        tuple: (is_valid, error_message)
    """
    try:
        df = pd.read_csv(file)
        required_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'pH', 'rainfall', 'timestamp']
        
        # Check for required columns
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            return False, f"Missing required columns: {', '.join(missing_columns)}"
        
        # Check for empty data
        if df.empty:
            return False, "CSV file is empty"
        
        # Try to convert timestamp
        try:
            pd.to_datetime(df['timestamp'])
        except:
            return False, "Invalid timestamp format"
        
        return True, ""
        
    except Exception as e:
        return False, f"Error validating CSV: {str(e)}"