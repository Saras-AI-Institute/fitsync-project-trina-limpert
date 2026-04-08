import pandas as pd


def load_data():
    """
    Load health data from the CSV, handle missing values, and return the cleaned DataFrame.

    Returns:
        pd.DataFrame: Cleaned health data.
    """
    # Path to the CSV file
    file_path = 'data/health_data.csv'
    
    # Load the data into a DataFrame
    df = pd.read_csv(file_path)
    
    # Fill missing Steps values with the median of Steps
    steps_median = df['Steps'].median()
    df['Steps'].fillna(steps_median, inplace=True)

    # Fill missing Sleep_Hours with 7.0
    df['Sleep_Hours'].fillna(7.0, inplace=True)

    # Fill missing Heart_Rate_bpm with 68
    df['Heart_Rate_bpm'].fillna(68, inplace=True)

    # Fill missing values in other columns with their median
    for column in ['Calories_Burned', 'Active_Minutes']:
        median_value = df[column].median()
        df[column].fillna(median_value, inplace=True)

    # Convert 'Date' column to datetime object
    df['Date'] = pd.to_datetime(df['Date'])

    # Return the cleaned DataFrame
    return df


def calculate_recovery_score(df):
    """
    Calculate and add a 'Recovery_Score' column to the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing health data.

    Returns:
        pd.DataFrame: DataFrame with added 'Recovery_Score' column.
    """

    # Initialize the Recovery_Score column with a base score of 50 for all entries
    df['Recovery_Score'] = 50

    # Adjust score based on Sleep_Hours
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20  # Boost score for good sleep
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 20   # Reduce score for poor sleep

    # Adjust score based on Heart_Rate_bpm
    # Normalize heart rate by assuming 95 is bad and 50 is optimal
    df['Recovery_Score'] += (95 - df['Heart_Rate_bpm']) / 5  # Scale heart rate impact

    # Adjust score based on Steps
    # Normalize steps assuming 12000 is the threshold where more steps start adding strain
    df['Recovery_Score'] -= (df['Steps'] - 12000) / 1000  # Moderate penalty for very high steps

    # Ensure the score stays within the bounds of 0 and 100
    df['Recovery_Score'] = df['Recovery_Score'].clip(lower=0, upper=100)

    return df


def process_data():
    """
    Main function to process health data and prepare it for the Streamlit dashboard.

    Returns:
        pd.DataFrame: Processed health data with Recovery Score.
    """
    df = load_data()  # Load and clean the data
    df = calculate_recovery_score(df)  # Add the Recovery Score
    return df  # Return the processed DataFrame

