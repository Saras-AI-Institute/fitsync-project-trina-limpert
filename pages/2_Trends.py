import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide", page_title="Trends & Insights")

# Title
st.title("Trends & Insights")

# Load and process data
@st.cache_data
def get_processed_data():
    return process_data()

processed_data = get_processed_data()

# Sidebar filter
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Filter the dataframe based on the selected time range
df = processed_data.copy()
if time_range == "Last 7 Days":
    recent_date = df['Date'].max()
    df = df[df['Date'] >= (recent_date - pd.Timedelta(days=7))]
elif time_range == "Last 30 Days":
    recent_date = df['Date'].max()
    df = df[df['Date'] >= (recent_date - pd.Timedelta(days=30))]

# Summary statistics
# Removing the subtitle
st.dataframe(df[['Recovery_Score', 'Sleep_Hours', 'Steps', 'Calories_Burned']].agg(['mean', 'max']))

# Average Recovery Score month-wise
# Removed the subtitle
df['month'] = df['Date'].dt.to_period('M')
avg_recovery_month = df.groupby('month')['Recovery_Score'].mean().reset_index()
avg_recovery_month['month'] = avg_recovery_month['month'].astype(str)

# Create a line chart for average recovery score by month
recovery_line_fig = px.line(
    avg_recovery_month, 
    x='month', 
    y='Recovery_Score', 
    title='Average Recovery Score by Month',
    labels={'month': 'Month', 'Recovery_Score': 'Average Recovery Score'})
st.plotly_chart(recovery_line_fig, use_container_width=True)

# Remove subtitle for histograms
df_metrics = ['Steps', 'Calories_Burned', 'Recovery_Score', 'Sleep_Hours']

for metric in df_metrics:
    histogram_fig = px.histogram(
        df, 
        x=metric, 
        title=f'Distribution of {metric}',
        labels={metric: metric})
    st.plotly_chart(histogram_fig, use_container_width=True)