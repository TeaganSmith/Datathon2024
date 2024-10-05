import geopandas as gpd

# Load shapefile for counties
counties = gpd.read_file('115795-V3/AgChange/AgChange/shapefiles/US_counties_2012_geoid.shp')

# Preview the data
print(counties.head())

