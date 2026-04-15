import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide", page_title="FitSync")

# Title
st.title("FitSync - Personal Health Analytics")

# Process the data to be used in the dashboard
processed_data = process_data()

# Display the processed data in a clean and modern way
#st.dataframe(processed_data)  # You can extend this part to include more insights

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

# Create columns for charts
chart_col1, chart_col2 = st.columns(2)

# Left column - Dual Line Chart
with chart_col1:
    st.subheader("Recovery Score & Sleep Trend")

    # Creating line chart for Recovery Score and Sleep Hours
    line_fig = px.line(
        df,
        x='Date',
        y=['Recovery_Score', 'Sleep_Hours'],
        title="Recovery Score & Sleep Trend",
        labels={'value': 'Score/Hours', 'variable': 'Metrics'})
    st.plotly_chart(line_fig, use_container_width=True)

# Right column - Scatter Plot
with chart_col2:
    st.subheader("Recovery Score vs Daily Steps")

    # Creating scatter plot
    scatter_fig = px.scatter(
        df,
        x='Steps',
        y='Recovery_Score',
        color='Sleep_Hours',
        title="Recovery Score vs Daily Steps",
        labels={'Steps': 'Daily Steps', 'Recovery_Score': 'Recovery Score'})
    st.plotly_chart(scatter_fig, use_container_width=True)

# Add a separator between chart sections
st.markdown("---")

# Create second set of columns for additional charts
chart_col3, chart_col4 = st.columns(2)

# Left column - Recovery Score vs Heart Rate
with chart_col3:
    st.subheader("Recovery Score vs Resting Heart Rate")

    # Scatter plot for Recovery Score vs Resting Heart Rate
    heart_rate_fig = px.scatter(
        df,
        x='Heart_Rate_bpm',
        y='Recovery_Score',
        title="Recovery Score vs Resting Heart Rate",
        labels={'Heart_Rate_bpm': 'Resting Heart Rate (bpm)', 'Recovery_Score': 'Recovery Score'})
    st.plotly_chart(heart_rate_fig, use_container_width=True)

# Right column - Line Chart for Calories Burned
with chart_col4:
    st.subheader("Daily Calories Burned Trend")

    # Line chart for Calories Burned Trend
    calories_fig = px.line(
        df,
        x='Date',
        y='Calories_Burned',
        title="Daily Calories Burned Trend",
        labels={'Calories_Burned': 'Calories Burned'})
    st.plotly_chart(calories_fig, use_container_width=True)

# Placeholder for future enhancements
# e.g. charts, interactive elements etc.