import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load your CSV file
file_path = 'combined_monarch_sightings_filled.csv'  # Replace with your file path
data = pd.read_csv(file_path)


# Add a column for "day of the year" (1 to 365) based on the 'Date' column
data['Date'] = pd.to_datetime(data['Date'])
data['day_of_year'] = data['Date'].dt.dayofyear

# Save the transformed data to a new CSV file
output_path = 'transformed_monarch_sightings.csv'
data.to_csv(output_path, index=False)

print("Data transformation complete. Saved to:", output_path)