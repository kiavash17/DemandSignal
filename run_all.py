
import subprocess
import time
import os
import platform
import redis

def check_and_start_redis():
    try:
        # Check if Redis is running
        r = redis.StrictRedis(host='localhost', port=6379)
        r.ping()
        print("Redis server is running.")
    except redis.exceptions.ConnectionError:
        print("Redis server is not running. Attempting to start Redis...")
        if platform.system() == "Linux":
            os.system("sudo service redis-server start")
        elif platform.system() == "Darwin":  # macOS
            os.system("brew services start redis")
        elif platform.system() == "Windows":
            os.system("Start-Service -Name Redis")

def run_backend():
    return subprocess.Popen(['python', 'backend.py'])

def run_frontend():
    return subprocess.Popen(['streamlit', 'run', 'app.py'])

if __name__ == "__main__":
    # Check and start Redis if necessary
    check_and_start_redis()

    print("Starting Flask backend...")
    backend_process = run_backend()
    time.sleep(2)

    print("Starting Streamlit frontend...")
    frontend_process = run_frontend()

    try:
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("Shutting down...")
        backend_process.terminate()
        frontend_process.terminate()
