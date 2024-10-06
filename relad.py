import pandas as pd

# Load the monarch sightings dataset
df = pd.read_csv('monarch_sightings2021_with_fips.csv')

# Ensure 'FIPS' is of type string
df['FIPS'] = pd.to_numeric(df['FIPS'], errors='coerce').astype('Int64')  # Convert to integers
df['FIPS'] = df['FIPS'].astype(str).str.zfill(5)  # Zero-pad FIPS codes

# Keep the relevant columns
df = df[['Town', 'State/Province', 'County', 'Count', 'Latitude', 'Longitude', 'FIPS']]

# Aggregate the sightings count by FIPS
df_county_sightings = df.groupby(['FIPS']).agg({'Count': 'sum'}).reset_index()

# Find the maximum sightings
max_sightings = df_county_sightings['Count'].max()

# Calculate the average sightings
average_sightings = df_county_sightings['Count'].mean()

# Optionally, find the county with the maximum sightings
max_county_row = df_county_sightings[df_county_sightings['Count'] == max_sightings]

# Print the results
print(f'Maximum butterfly sightings across all counties: {max_sightings}')
print(f'Average butterfly sightings across all counties: {average_sightings:.2f}')
print(f'County with maximum sightings:\n{max_county_row}')
