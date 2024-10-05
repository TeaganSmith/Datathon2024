import geopandas as gpd
import matplotlib.pyplot as plt

# Step 1: Load the shapefile for U.S. counties
counties = gpd.read_file('115795-V3/AgChange/AgChange/shapefiles/US_counties_2012_geoid.shp')

# Step 2: Plot the counties
counties.plot()

# Step 3: Show the plot
plt.show()