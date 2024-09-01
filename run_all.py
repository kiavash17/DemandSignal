
import subprocess
import time

def run_backend():
    # Run the Flask backend
    return subprocess.Popen(['python', 'backend.py'])

def run_frontend():
    # Run the Streamlit frontend
    return subprocess.Popen(['streamlit', 'run', 'app.py'])

if __name__ == "__main__":
    # Start the backend
    print("Starting Flask backend...")
    backend_process = run_backend()
    time.sleep(2)  # Wait a few seconds to ensure the backend starts properly

    # Start the frontend
    print("Starting Streamlit frontend...")
    frontend_process = run_frontend()

    try:
        # Keep the script running to keep both processes alive
        backend_process.wait()
        frontend_process.wait()
    except KeyboardInterrupt:
        print("Shutting down...")
        backend_process.terminate()
        frontend_process.terminate()
