import pandas as pd

# Load the CSV file
file_path = "combined_monarch_sightings_filled.csv"
data = pd.read_csv(file_path)

# Filter out rows where 'Count' is greater than 100
data_filtered = data[data['Count'] <= 20]

# Save the filtered data to a new CSV file
output_file_path = "filtered_monarch_sightings.csv"
data_filtered.to_csv(output_file_path, index=False)

print(f"Filtered data saved to {output_file_path}")
