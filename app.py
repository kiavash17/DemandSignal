import streamlit as st
import requests
from datetime import datetime
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objects as go
import json

# Define backend URL (ensure this matches your backend server's address)
BACKEND_URL = "http://localhost:5000"

# Streamlit page configuration
st.set_page_config(page_title="ExplorerBee Dashboard", layout="wide")

# Page title
st.title("ExplorerBee: AI-Driven Demand Forecasting")

# Sidebar for startup information input
st.sidebar.header("Enter Startup Information")
company_name = st.sidebar.text_input("Company Name")
industry = st.sidebar.text_input("Industry")
uvp = st.sidebar.text_area("Unique Value Proposition (UVP)")
target_audience = st.sidebar.text_area("Target Audience")

if st.sidebar.button("Submit"):
    # Sending startup data to the backend for processing
    response = requests.post(f"{BACKEND_URL}/submit_startup", data={
        'company_name': company_name,
        'industry': industry,
        'uvp': uvp,
        'target_audience': target_audience
    })

    if response.status_code == 200:
        st.sidebar.success("Startup information submitted successfully!")
    else:
        st.sidebar.error("Failed to submit startup information. Please try again.")

# Fetch trend data from backend
st.header("Trend Analysis")
keyword = st.text_input("Enter a keyword to analyze:")
if st.button("Fetch Trend Data"):
    response = requests.get(f"{BACKEND_URL}/fetch_trend_data", params={"keyword": keyword})
    
    if response.status_code == 200:
        trend_data = response.json()
        df_trend = pd.DataFrame(trend_data)
        st.write(df_trend)

        # Plot trend data
        st.line_chart(df_trend['value'])

        # Forecasting with Prophet
        df_trend['ds'] = pd.to_datetime(df_trend['date'])
        df_trend['y'] = df_trend['value']
        m = Prophet()
        m.fit(df_trend[['ds', 'y']])
        future = m.make_future_dataframe(periods=30)
        forecast = m.predict(future)
        fig = plot_plotly(m, forecast)
        st.plotly_chart(fig)
    else:
        st.error("Failed to fetch trend data. Please try again.")

# Fetch analytics data from backend
st.header("Outreach and A/B Testing Analytics")
if st.button("Load Analytics Data"):
    response = requests.get(f"{BACKEND_URL}/analytics_data")
    
    if response.status_code == 200:
        analytics_data = response.json()

        # Display A/B test results
        st.subheader("A/B Test Results")
        ab_test_results = analytics_data.get("ab_test_results", {})
        st.json(ab_test_results)

        # Plot A/B test results
        ab_test_df = pd.DataFrame(list(ab_test_results.items()), columns=['Version', 'Interested'])
        fig = go.Figure(data=[go.Bar(x=ab_test_df['Version'], y=ab_test_df['Interested'])])
        st.plotly_chart(fig)

        # Display refinement suggestions
        st.subheader("Refinement Suggestions")
        refinement_suggestions = analytics_data.get("refinement_suggestions", "No suggestions available.")
        st.write(refinement_suggestions)
    else:
        st.error("Failed to load analytics data. Please try again.")

# Footer with contact information
st.write("---")
st.write("For support, contact us at [support@explorerbee.com](mailto:support@explorerbee.com).")
