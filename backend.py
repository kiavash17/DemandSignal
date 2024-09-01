from flask import Flask, request, jsonify
from flask_executor import Executor
import pandas as pd

app = Flask(__name__)
executor = Executor(app)

# Simulated user data (for demonstration purposes)
users = {"user1": "password1", "user2": "password2"}

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
def get_trend_data():
    try:
        # Call the function to fetch data
        trend_data = fetch_trend_data_async()
        return jsonify(trend_data), 200
    except Exception as e:
        return jsonify({"message": f"Error fetching trend data: {str(e)}"}), 500

def fetch_trend_data_async():
    # Load data and convert it to a dictionary format
    trend_data = pd.read_csv('data_storage/simulated_google_trends_data.csv')
    return trend_data.to_dict(orient='records')

if __name__ == "__main__":
    app.run(debug=True)
