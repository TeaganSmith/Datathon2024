import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the monarch sightings dataset
df = pd.read_csv('monarch_sightings2021_with_fips.csv')

# Ensure 'FIPS' is of type string
df['FIPS'] = pd.to_numeric(df['FIPS'], errors='coerce').astype('Int64')  # Convert to integers
df['FIPS'] = df['FIPS'].astype(str).str.zfill(5)  # Zero-pad FIPS codes

# Keep the relevant columns
df = df[['Town', 'State/Province', 'County', 'Count', 'Latitude', 'Longitude', 'FIPS']]

# Aggregate the sightings count by FIPS
df_county_sightings = df.groupby(['FIPS']).agg({'Count': 'sum'}).reset_index()

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

# Normalize the Count using a logarithmic scale
counties_sightings['log_count'] = np.log1p(counties_sightings['Count'])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# First, plot all counties with a light color for the borders
counties.boundary.plot(ax=ax, linewidth=0.5, color='black')

# Plot using the log-scaled count
counties_sightings.plot(column='log_count', ax=ax, legend=True, linewidth=0.8, edgecolor='0.8', cmap='OrRd',
                        vmin=0, vmax=counties_sightings['log_count'].max(),
                        missing_kwds={
                            "color": "white",  # Color for counties without sightings
                            "edgecolor": "white",
                            "hatch": "//"  # Optional: pattern for counties without sightings
                        })

# Set the aspect ratio and add title
ax.set_aspect('auto')
ax.set_title('Monarch Sightings by County (Log Scale)', fontsize=15)

# Display the plot
plt.show()
