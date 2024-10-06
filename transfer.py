import pandas as pd

# Load the datasets
monarch_sightings_path = 'csv-files-data/2016/monarch_sightings2016_detailed.csv'
aqi_data_path = 'daily_aqi_by_county_2016/daily_aqi_by_county_2016.csv'

# Load the CSV files
monarch_sightings_df = pd.read_csv(monarch_sightings_path)
aqi_data_df = pd.read_csv(aqi_data_path)

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
aqi_data_df.rename(columns={
    'State Name': 'State/Province',
    'county Name': 'County',
    'Date': 'Date',
    'AQI': 'AQI'
}, inplace=True)

# Convert Date columns to datetime for proper merging
monarch_sightings_df['Date'] = pd.to_datetime(monarch_sightings_df['Date'])
aqi_data_df['Date'] = pd.to_datetime(aqi_data_df['Date'])

# Replace state names with abbreviations in both datasets
aqi_data_df['State/Province'] = aqi_data_df['State/Province'].map(state_abbreviations)

# Normalize County names (ignore case, strip spaces)
monarch_sightings_df['County'] = monarch_sightings_df['County'].str.lower().str.strip()
aqi_data_df['County'] = aqi_data_df['County'].str.lower().str.strip()

# Merge the two dataframes based on 'State/Province', 'County', and 'Date'
# Exclude the 'Category' field, only keep the AQI field.
merged_df = pd.merge(monarch_sightings_df, 
                     aqi_data_df[['State/Province', 'County', 'Date', 'AQI']],
                     on=['State/Province', 'County', 'Date'], 
                     how='left')

# Save the merged dataset to a new CSV file
merged_df.to_csv('csv-files-data/2016/daily_aqi_data2016.csv', index=False)

print("The merged dataset has been saved to 'daily_aqi_data.csv'.")
