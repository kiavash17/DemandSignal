
import streamlit as st
import pandas as pd
import numpy as np
import requests
from textblob import TextBlob

# Backend URL
BACKEND_URL = "http://localhost:5000"

@st.cache
def fetch_trend_data():
    try:
        response = requests.get(f"{BACKEND_URL}/trend_data")
        if response.status_code == 200:
            trend_data = pd.read_json(response.content)
            return trend_data
        else:
            st.error("Failed to fetch trend data from the backend.")
            return None
    except Exception as e:
        st.error(f"Error fetching trend data: {e}")
        return None

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
if 'trend_data' not in st.session_state:
    trend_data = fetch_trend_data()
    if trend_data is not None:
        st.session_state['trend_data'] = trend_data
else:
    trend_data = st.session_state['trend_data']

if trend_data is not None:
    st.line_chart(trend_data.set_index('date'))

st.header('Sentiment Analysis')
sentiment_data = fetch_sentiment_data()
st.write(sentiment_data)

st.header('Download Data')
if trend_data is not None:
    st.download_button(label="Download trend data as CSV", data=trend_data.to_csv(index=False), mime='text/csv')

st.header('Predictive Analytics')
st.write("Predictive analytics will be added here.")
