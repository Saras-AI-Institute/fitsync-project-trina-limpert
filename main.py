import streamlit as st
from modules.processor import process_data
import pandas as pd

# Set page configuration
st.set_page_config(layout="wide", page_title="FitSync")

# Title
st.title("FitSync - Personal Health Analytics")

# Process the data to be used in the dashboard
processed_data = process_data()

# Display the processed data in a clean and modern way
st.dataframe(processed_data)  # You can extend this part to include more insights

# Sidebar filter
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Filter the dataframe based on the selected time range
df = process_data()
if time_range == "Last 7 Days":
    # Keep only the most recent 7 days
    recent_date = df['Date'].max()
    df = df[df['Date'] >= (recent_date - pd.Timedelta(days=7))]
elif time_range == "Last 30 Days":
    # Keep only the most recent 30 days
    recent_date = df['Date'].max()
    df = df[df['Date'] >= (recent_date - pd.Timedelta(days=30))]

# Recalculate metrics based on the filtered dataframe
average_steps = df['Steps'].mean()
average_sleep_hours = df['Sleep_Hours'].mean()
average_recovery_score = df['Recovery_Score'].mean()

# Create a 3-column layout
col1, col2, col3 = st.columns(3)

# Display updated metrics
with col1:
    st.metric(label="Average Steps", value=f"{average_steps:,.0f}", delta=None)

with col2:
    st.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)

with col3:
    st.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)

# Placeholder for future enhancements
# e.g. charts, interactive elements etc.