import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('monarch_sightings.csv')

# Group by year and calculate total sightings and average AQI
aggregated_data = data.groupby('Year').agg({
    'Count': 'sum',       # Sum monarch sightings by year
    'AQI': 'mean'         # Average AQI by year
}).reset_index()

plt.figure(figsize=(10, 6))
plt.plot(aggregated_data['Year'], aggregated_data['Count'], marker='o', color='blue', label='Monarch Sightings')
plt.xlabel('Year')
plt.ylabel('Total Monarch Sightings')
plt.title('Monarch Butterfly Sightings by Year')
plt.grid(True)
plt.legend()
plt.show()