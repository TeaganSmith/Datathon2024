import pandas as pd

# Load the CSV file
file_path = "combined_monarch_sightings_filled.csv"
data = pd.read_csv(file_path)

# Display basic statistics of the 'Count' column
print("Summary statistics of the 'Count' field:")
print(data['Count'].describe())

# Calculate IQR for the 'Count' field
Q1 = data['Count'].quantile(0.25)
Q99 = data['Count'].quantile(0.95)
IQR = Q99 - Q1

# Define outlier threshold
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q99 + 1.5 * IQR

# Remove outliers from the data
data_no_outliers = data[(data['Count'] >= lower_bound) & (data['Count'] <= upper_bound)]

# Calculate the mean and standard deviation without outliers
mean_no_outliers = data_no_outliers['Count'].mean()
std_no_outliers = data_no_outliers['Count'].std()

# Print the results
print(f"Mean without outliers: {mean_no_outliers}")
print(f"Standard deviation without outliers: {std_no_outliers}")
