import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Load your dataset (replace with your file path)
data = pd.read_csv('transformed_monarch_sightings.csv')

# Filter for counties with sufficient data across seasons
counties_with_sufficient_data = data.groupby('County').filter(lambda x: x['season'].nunique() > 1)

# ANOVA: Check if there's a significant difference in monarch count by season and temperature
anova_results = {}

# Perform ANOVA for each county
for county in counties_with_sufficient_data['County'].unique():
    county_data = counties_with_sufficient_data[counties_with_sufficient_data['County'] == county]
    
    # Perform one-way ANOVA for count based on temperature across seasons
    groups = [county_data['Count'][county_data['season'] == season] for season in county_data['season'].unique()]
    
    # Ensure that each season has enough data points to perform ANOVA
    if all(len(group) > 1 for group in groups):
        anova_result = stats.f_oneway(*groups)
        anova_results[county] = anova_result.pvalue

# Print the ANOVA results (p-values)
print("ANOVA Results (p-values):")
for county, pvalue in anova_results.items():
    print(f"{county}: {pvalue}")

# Select top counties for visualization (based on availability of data)
top_counties = counties_with_sufficient_data['County'].value_counts().index[:3]

# Plotting monarch counts and temperature across seasons for selected counties
plt.figure(figsize=(15, 8))
for i, county in enumerate(top_counties):
    county_data = counties_with_sufficient_data[counties_with_sufficient_data['County'] == county]
    
    plt.subplot(1, 3, i + 1)
    for season in county_data['season'].unique():
        season_data = county_data[county_data['season'] == season]
        plt.scatter(season_data['Temp_Mean'], season_data['Count'], label=season)
    
    plt.title(f'Monarch Count vs Temp by Season in {county.capitalize()}')
    plt.xlabel('Mean Temperature (°F)')
    plt.ylabel('Monarch Count')
    plt.legend(title="Season")

plt.tight_layout()
plt.show()
