import pandas as pd

# Define a variable for the year to be used in filenames
year = '2010'

# Load the datasets
monarch_sightings_path = f'csv-files-data/{year}/daily_aqi_data{year}.csv'
temp_data_path = f'daily_TEMP_{year}/daily_TEMP_{year}.csv'

# Load the CSV files
monarch_sightings_df = pd.read_csv(monarch_sightings_path)
temp_data_df = pd.read_csv(temp_data_path)

# Dictionary to map full state names to abbreviations
state_abbreviations = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

# Standardizing the column names for merging
temp_data_df.rename(columns={
    'State Name': 'State/Province',
    'County Name': 'County',
    'Date Local': 'Date',
    'Arithmetic Mean': 'Temp_Mean'
}, inplace=True)

# Convert Date columns to datetime for proper merging
monarch_sightings_df['Date'] = pd.to_datetime(monarch_sightings_df['Date'])
temp_data_df['Date'] = pd.to_datetime(temp_data_df['Date'])

# Replace state names with abbreviations in both datasets
temp_data_df['State/Province'] = temp_data_df['State/Province'].map(state_abbreviations)

# Normalize County names: lowercased, stripped of spaces
monarch_sightings_df['County'] = monarch_sightings_df['County'].str.lower().str.replace(r'\s+', '', regex=True)
temp_data_df['County'] = temp_data_df['County'].str.lower().str.replace(r'\s+', '', regex=True)

# Aggregate temperature data to prevent duplicates, e.g., using the mean temperature for each combination
temp_data_df_agg = temp_data_df.groupby(['State/Province', 'County', 'Date'], as_index=False).agg({
    'Temp_Mean': 'mean'  # You can change to 'first' if you want the first available value instead of the mean
})

# Merge the two dataframes based on 'State/Province', 'County', and 'Date'
merged_df = pd.merge(monarch_sightings_df, 
                     temp_data_df_agg[['State/Province', 'County', 'Date', 'Temp_Mean']],
                     on=['State/Province', 'County', 'Date'], 
                     how='left')

# Save the merged dataset to a new CSV file, using the 'year' variable
merged_df.to_csv(f'csv-files-data/{year}/daily_temp_data{year}.csv', index=False)

print(f"The merged dataset has been saved to 'daily_temp_data{year}.csv'.")
