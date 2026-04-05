import pandas as pd

# Adjust pandas display options to show all columns
pd.set_option('display.max_columns', None)

# Load the health data from CSV
file_path = 'data/health_data.csv'
try:
    health_data = pd.read_csv(file_path)
    
    # Print the first 5 rows
    print("First 5 rows of the dataset:")
    print(health_data.head())
    
    # Calculate and print the number of missing values in each column
    print("\nNumber of missing values in each column:")
    print(health_data.isnull().sum())
except FileNotFoundError:
    print(f"File not found: {file_path}")