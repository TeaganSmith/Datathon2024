import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the monarch sightings dataset
df = pd.read_csv('monarch_sightings_with_fips_zero_padded.csv')

# Ensure 'FIPS' is of type string
df['FIPS'] = pd.to_numeric(df['FIPS'], errors='coerce').astype('Int64')  # Convert to integers
df['FIPS'] = df['FIPS'].astype(str).str.zfill(5)  # Zero-pad FIPS codes

# Keep the relevant columns
df = df[['city', 'state', 'county', 'count', 'FIPS', 'cleaned_county']]

# Aggregate the sightings count by FIPS
df_county_sightings = df.groupby(['FIPS']).agg({'count': 'sum'}).reset_index()

# Load the shapefile for counties
counties = gpd.read_file('115795-V3/AgChange/AgChange/shapefiles/US_counties_2012_geoid.shp')

# Ensure 'FIPS' in the shapefile is also a string
counties['FIPS'] = counties['FIPS'].astype(str)

# Merge the aggregated sightings data with the county geometries
counties_sightings = counties.merge(df_county_sightings, left_on='FIPS', right_on='FIPS', how='left')

# Drop rows with missing FIPS or missing geometry
counties_sightings = counties_sightings.dropna(subset=['FIPS', 'geometry'])

# Drop rows with invalid geometries
counties_sightings = counties_sightings[counties_sightings.is_valid]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# First, plot all counties with a light color for the borders
counties.boundary.plot(ax=ax, linewidth=0.5, color='black')  # Plot county borders

# Then plot the counties with sightings and color them based on the count of monarch sightings
counties_sightings.plot(column='count', ax=ax, legend=True, linewidth=0.8, edgecolor='0.8', cmap='OrRd', missing_kwds={
    "color": "white",  # Color for counties without sightings
    "edgecolor": "white",
    "hatch": "//"  # Optional: pattern for counties without sightings
})

# Set the aspect ratio to 'auto' to avoid aspect-related errors
ax.set_aspect('auto')

# Add title
ax.set_title('Monarch Sightings by County', fontsize=15)

# Display the plot
plt.show()
