
import streamlit as st
import pandas as pd
import requests
from textblob import TextBlob
from prophet import Prophet
import matplotlib.pyplot as plt

# Backend URL
BACKEND_URL = "http://localhost:5000"

@st.cache
def fetch_trend_data():
    try:
        response = requests.get(f"{BACKEND_URL}/trend_data")
        if response.status_code == 200:
            trend_data = pd.DataFrame(response.json())
            return trend_data
        else:
            st.error(f"Failed to fetch trend data from the backend. Error: {response.text}")
            return None
    except Exception as e:
        st.error(f"Error fetching trend data: {e}")
        return None

@st.cache
def fetch_financial_data(ticker='AAPL'):
    try:
        response = requests.get(f"{BACKEND_URL}/financial_data", params={'ticker': ticker})
        if response.status_code == 200:
            financial_data = pd.DataFrame(response.json())
            return financial_data
        else:
            st.error(f"Failed to fetch financial data from the backend. Error: {response.text}")
            return None
    except Exception as e:
        st.error(f"Error fetching financial data: {e}")
        return None

@st.cache
def fetch_social_media_data(query='biotech'):
    try:
        response = requests.get(f"{BACKEND_URL}/social_media_data", params={'query': query})
        if response.status_code == 200:
            social_media_data = pd.DataFrame(response.json())
            return social_media_data
        else:
            st.error(f"Failed to fetch social media data from the backend. Error: {response.text}")
            return None
    except Exception as e:
        st.error(f"Error fetching social media data: {e}")
        return None

def forecast_demand(trend_data):
    # Prepare data for Prophet
    trend_data.rename(columns={'date': 'ds', 'AI': 'y'}, inplace=True)
    model = Prophet()
    model.fit(trend_data[['ds', 'y']])
    
    # Make future dataframe and predict
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast

def fetch_sentiment_data():
    simulated_posts = [
        "AI is revolutionizing biotech with new discoveries every day!",
        "Machine learning is helping solve some of the hardest problems in science.",
        "Biotech stocks are on the rise due to AI advancements.",
        "There are concerns about the ethical implications of AI in healthcare.",
        "Exciting times ahead with the intersection of AI and biotechnology."
    ]
    
    sentiment_scores = [TextBlob(text).sentiment.polarity for text in simulated_posts]
    
    sentiment_df = pd.DataFrame({
        'post': simulated_posts,
        'sentiment_score': sentiment_scores
    })
    return sentiment_df

# Streamlit Dashboard
st.title('AI-Driven Demand Forecasting Dashboard')

st.header('Trend Analysis')
trend_data = fetch_trend_data()
if trend_data is not None:
    st.line_chart(trend_data.set_index('date'))

    # Forecasting Section
    st.header('Demand Forecasting')
    forecast = forecast_demand(trend_data)
    fig, ax = plt.subplots()
    model = Prophet()
    model.plot(forecast, ax=ax)
    st.pyplot(fig)

st.header('Financial Data Analysis')
financial_data = fetch_financial_data()
if financial_data is not None:
    st.line_chart(financial_data.set_index('Date')['Close'])

st.header('Social Media Sentiment Analysis')
social_media_data = fetch_social_media_data()
if social_media_data is not None:
    st.write(social_media_data)

st.header('Sentiment Analysis')
sentiment_data = fetch_sentiment_data()
st.write(sentiment_data)

st.header('Download Data')
if trend_data is not None:
    st.download_button(label="Download trend data as CSV", data=trend_data.to_csv(index=False), mime='text/csv')

st.header('Predictive Analytics')
st.write("Predictive analytics will be added here.")
