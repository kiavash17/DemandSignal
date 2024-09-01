
import os
import pandas as pd
import numpy as np

# Directory and file path
directory = 'data_storage'
file_path = os.path.join(directory, 'simulated_google_trends_data.csv')

# Create directory if it does not exist
os.makedirs(directory, exist_ok=True)

# Sample data for the CSV file
trend_data = pd.DataFrame({
    'date': pd.date_range(start='2024-01-01', periods=90, freq='D'),
    'AI': np.random.randint(50, 100, size=(90,)),
    'machine learning': np.random.randint(50, 100, size=(90,)),
    'biotech': np.random.randint(50, 100, size=(90,))
})

# Save sample data to CSV file
trend_data.to_csv(file_path, index=False)
print(f"Sample data created at {file_path}")
