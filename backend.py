
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
    future = executor.submit(fetch_trend_data_async)
    result = future.result()
    return result

def fetch_trend_data_async():
    try:
        trend_data = pd.read_csv('data_storage/simulated_google_trends_data.csv')
        return trend_data.to_json(orient='records'), 200
    except Exception as e:
        return jsonify({"message": f"Error fetching trend data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
