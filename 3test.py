import pandas as pd

# Load the dataset
data = pd.read_csv("combined_monarch_sightings_filled.csv")

# Calculate the count of missing values in each column
missing_count = data.isnull().sum()

# Calculate the percentage of missing values in each column
missing_percentage = (data.isnull().sum() / len(data)) * 100

# Normalize missing data by filling it with the mean of each numeric column (except Temp_Mean and AQI)
data_filled = data

# Replace Temp_Mean missing values with the average temperature of the corresponding year, season, and state
data_filled['Temp_Mean'] = data.groupby(['year', 'season', 'State/Province'])['Temp_Mean'].transform(lambda x: x.fillna(x.mean()))

# Replace missing AQI values with the average AQI of the corresponding year, season, and state
data_filled['AQI'] = data_filled.groupby(['year', 'season', 'State/Province'])['AQI'].transform(lambda x: x.fillna(x.mean()))

# Create a summary DataFrame to show count and percentage of missing values
missing_data_summary = pd.DataFrame({
    'Missing Count': missing_count,
    'Missing Percentage (%)': missing_percentage
})

# Display the summary of missing data
print(missing_data_summary)

# Save the filled dataset to a new CSV file
data_filled.to_csv("combined_monarch_sightings_filled.csv", index=False)

# Show the first few rows of the filled data to verify
print(data_filled.head())
