
# AI-Driven Demand Forecasting Dashboard (Versioned)

This repository contains the AI-Driven Demand Forecasting platform, which now includes integrated advanced predictive analytics, financial data, and social media sentiment analysis, along with a unified script to run both the backend and frontend applications.

## Features

- **Trend Analysis**: Visualize trends over time for different keywords using data fetched from a Flask backend.
- **Demand Forecasting**: Predict future trends using Facebook Prophet's time series forecasting model.
- **Financial Data Integration**: Analyze financial market data using Yahoo Finance API.
- **Social Media Sentiment Analysis**: Perform sentiment analysis on real-time tweets related to specific market trends.
- **Unified Execution**: A single script (`run_all.py`) to run both the backend and frontend simultaneously, streamlining the development workflow.
- **Predictive Analytics**: Placeholder for future predictive analytics features.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Redis server (for caching purposes)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/ai-demand-forecasting-v1.git
   cd ai-demand-forecasting-v1
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the App

1. **Data Preparation**:
   - Generate sample data if not already present by running:
   ```
   python create_data.py
   ```

2. **Unified Execution**:
   - Run both the Flask backend and Streamlit frontend with a single command:
   ```
   python run_all.py
   ```

   This script will start the backend and frontend together, making the development process more efficient.

### Deployment

To deploy the app on Streamlit Community Cloud or another platform, follow the steps in the README file.

### Future Enhancements

- **Machine Learning Models**: Additional predictive models for enhanced forecasting.
- **Expanded Data Sources**: More data sources for comprehensive demand insights.
- **User Authentication and Management**: Enhanced security and user management features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
