import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the monarch sightings dataset
file_path = 'monarch_sightings_csv/monarch_sightings2010_with_fips.csv'
df = pd.read_csv(file_path)
file_name = os.path.basename(file_path)
year = file_name[17:21]

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

# Plot all counties with a light color for the borders
counties.boundary.plot(ax=ax, linewidth=0.5, color='black')

# Plot using the log-scaled count
pc = counties_sightings.plot(column='log_count', ax=ax, linewidth=0.8, edgecolor='0.8', cmap='OrRd',
                             vmin=0, vmax=counties_sightings['log_count'].max(),
                             missing_kwds={
                                 "color": "white",  # Color for counties without sightings
                                 "edgecolor": "white",
                                 "hatch": "//"  # Optional: pattern for counties without sightings
                             })

# Set the aspect ratio and add title
ax.set_aspect('auto')
ax.set_title('Monarch Butterfly sightings in ' + (year), fontsize=15)

# Create a colorbar manually
sm = plt.cm.ScalarMappable(cmap='OrRd', norm=plt.Normalize(vmin=0, vmax=counties_sightings['log_count'].max()))
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label('Count of Monarch Sightings')  # Add label to the colorbar

# Calculate min and max sightings
max_sightings = df_county_sightings['Count'].max()
min_sightings = df_county_sightings['Count'].min()

# Create a dynamic range for ticks
log_ticks = np.linspace(np.log1p(min_sightings), np.log1p(max_sightings), num=6)  # 6 ticks between log(min) and log(max)

# Set the ticks to logarithmic values
cbar.set_ticks(log_ticks)

# Set corresponding labels for the ticks based on the actual counts
tick_labels = [int(np.expm1(tick)) for tick in log_ticks]  # Convert back from log scale to original counts
cbar.set_ticklabels(tick_labels)

# Display the plot
plt.show()
