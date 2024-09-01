
from flask import Flask, request, jsonify
from flask_executor import Executor
from flask_caching import Cache
import pandas as pd
import yfinance as yf
import tweepy

app = Flask(__name__)
executor = Executor(app)

# Configure caching with Redis
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
cache = Cache(app)

# Simulated user data (for demonstration purposes)
users = {"user1": "password1", "user2": "password2"}

# Twitter API credentials (replace with your own)
TWITTER_API_KEY = 'your_api_key'
TWITTER_API_SECRET = 'your_api_secret'
TWITTER_ACCESS_TOKEN = 'your_access_token'
TWITTER_ACCESS_SECRET = 'your_access_secret'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
        return jsonify({"message": "Login successful", "status": "success"}), 200
    else:
        return jsonify({"message": "Invalid credentials", "status": "failure"}), 401

@app.route('/trend_data', methods=['GET'])
@cache.cached(timeout=60)  # Cache this endpoint for 60 seconds
def get_trend_data():
    try:
        trend_data = fetch_trend_data_async()
        return jsonify(trend_data)
    except Exception as e:
        return jsonify({"message": f"Error fetching trend data: {str(e)}"}), 500

@app.route('/financial_data', methods=['GET'])
@cache.cached(timeout=60)  # Cache this endpoint for 60 seconds
def get_financial_data():
    try:
        ticker = request.args.get('ticker', 'AAPL')
        data = yf.download(ticker, period='1mo', interval='1d')
        data.reset_index(inplace=True)
        return data.to_dict(orient='records')
    except Exception as e:
        return jsonify({"message": f"Error fetching financial data: {str(e)}"}), 500

@app.route('/social_media_data', methods=['GET'])
@cache.cached(timeout=60)  # Cache this endpoint for 60 seconds
def get_social_media_data():
    try:
        query = request.args.get('query', 'biotech')
        tweets = api.search(q=query, count=100, lang='en', tweet_mode='extended')
        tweet_data = [{'text': tweet.full_text, 'created_at': tweet.created_at} for tweet in tweets]
        return jsonify(tweet_data)
    except Exception as e:
        return jsonify({"message": f"Error fetching social media data: {str(e)}"}), 500

def fetch_trend_data_async():
    trend_data = pd.read_csv('data_storage/simulated_google_trends_data.csv')
    return trend_data.to_dict(orient='records')

if __name__ == "__main__":
    app.run(debug=True)
