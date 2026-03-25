import pandas as pd
import numpy as np
from datetime import timedelta, date

# Function to generate dates
def generate_dates(start_date, days):
    return [start_date + timedelta(days=i) for i in range(days)]

# Generate 365 days of dates starting from 2025-01-01
dates = generate_dates(date(2025, 1, 1), 365)

# Generate realistic 365-day fitness data
np.random.seed(42)  # For reproducibility

steps = np.random.normal(loc=8500, scale=2000, size=365).clip(3000, 18000)
sleep_hours = np.random.normal(loc=7.2, scale=1, size=365).clip(4.5, 9.5)
heart_rate = np.random.normal(loc=68, scale=10, size=365).clip(48, 110)
calories_burned = np.random.randint(1800, 4200, size=365)
active_minutes = np.random.randint(20, 180, size=365)

# Introduce 5% missing values randomly in each column
def introduce_missing_values(data, percentage=0.05):
    n_values = int(len(data) * percentage)
    indices = np.random.choice(len(data), n_values, replace=False)
    data[indices] = np.nan
    return data

steps = introduce_missing_values(steps)
sleep_hours = introduce_missing_values(sleep_hours)
heart_rate = introduce_missing_values(heart_rate)
calories_burned = introduce_missing_values(calories_burned)
active_minutes = introduce_missing_values(active_minutes)

# Create dataframe
fitness_data = pd.DataFrame({
    'Date': dates,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Save to CSV
fitness_data.to_csv('data/health_data.csv', index=False)

print("Health data generated and saved to data/health_data.csv.")