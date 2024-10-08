import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.colors import LogNorm

# Load the monarch sightings dataset
file_path = 'monarch_sightings_csv/monarch_sightings2023_with_fips.csv'
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

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Plot all counties with a light color for the borders
counties.boundary.plot(ax=ax, linewidth=0.5, color='black')

# Get min and max counts for normalization
min_count = counties_sightings['Count'].min()
max_count = counties_sightings['Count'].max()

# Define the normalization using LogNorm
norm = LogNorm(vmin=1, vmax=10000)

# Plot using the log-scaled count with LogNorm
pc = counties_sightings.plot(column='Count', ax=ax, linewidth=0.8, edgecolor='0.8', cmap='YlOrRd',
                             norm=norm,
                             missing_kwds={
                                 "color": "white",  # Color for counties without sightings
                                 "edgecolor": "white",
                                 "hatch": "//"  # Optional: pattern for counties without sightings
                             })

# Set the aspect ratio and add title
ax.set_aspect('auto')
ax.set_title('USA Monarch Butterfly sightings in ' + year, fontsize=15)

# Create a colorbar with LogNorm
sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax)
cbar.set_label('Count of Monarch Sightings')  # Add label to the colorbar

# Create logarithmic ticks across 6 segments
# log_ticks = np.logspace(np.log10(min_count), np.log10(max_count), num=6).astype(int)

# # Set the ticks and labels on the colorbar
# cbar.set_ticks(log_ticks)
# cbar.set_ticklabels([str(tick) for tick in log_ticks])

# Customize the ticks and labels on the colorbar
log_ticks = [1, 10, 100, 1000, 5000, 10000]  # Standardized ticks
cbar.set_ticks(log_ticks)
cbar.set_ticklabels(['0', '10', '100', '1,000', '5,000', "10,000+"])


# Display the plot
plt.show()
