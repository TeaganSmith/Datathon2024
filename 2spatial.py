import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the monarch sightings dataset
df = pd.read_csv('monarch_sightings_with_fips_zero_padded.csv')

# Ensure 'FIPS' is of type string
df['FIPS'] = df['FIPS'].astype(str)

# Keep the relevant columns
df = df[['city', 'state', 'county', 'count', 'FIPS', 'cleaned_county']]

# Aggregate the sightings count by FIPS
df_county_sightings = df.groupby(['FIPS']).agg({'count': 'sum'}).reset_index()

# Load the shapefile for counties
counties = gpd.read_file('115795-V3/AgChange/AgChange/shapefiles/US_counties_2012_geoid.shp')

# Ensure 'FIPS' in the shapefile is also a string
counties['FIPS'] = counties['FIPS'].astype(str)

# Set CRS if it's not set
if counties.crs is None:
    counties = counties.set_crs('EPSG:4326')  # Common CRS for geographic data

# Transform counties to US National Atlas Equal Area projection EPSG:2163
counties = counties.to_crs('EPSG:2163')

# Ensure all geometries are valid
counties = counties[counties.is_valid]

# Merge the aggregated sightings data with the county geometries
counties_sightings = counties.merge(df_county_sightings, left_on='FIPS', right_on='FIPS')

# Load the US boundaries shapefile (you'll need to have this)
us_boundary = gpd.read_file('115795-V3/AgChange/AgChange/shapefiles/US_counties_2012_geoid.shp')

# Transform the boundary to the same CRS as counties
us_boundary = us_boundary.to_crs('EPSG:2163')

# Plot the counties and color them based on the count of monarch sightings
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

# Plot the US counties with monarch sightings
counties_sightings.plot(column='count', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Overlay only the boundary outline of the US map without filling
us_boundary.boundary.plot(ax=ax, color='black', linewidth=1.5)  # Only plot the outline, thicker border for visibility

# Set the aspect ratio to 'auto'
ax.set_aspect('auto')

# Add title
ax.set_title('Monarch Sightings by County with US Border', fontsize=15)

output_file = 'monarch_sightings_map_2024.png'  # Change the filename and extension as needed
plt.savefig(output_file, dpi=300, bbox_inches='tight')


# Display the plot
plt.show()
