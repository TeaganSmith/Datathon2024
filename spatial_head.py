import geopandas as gpd

# Load the shapefile
counties = gpd.read_file('115795-V3/AgChange/AgChange/shapefiles/US_counties_2012_geoid.shp')

# Check the structure of the data
print(counties.head())