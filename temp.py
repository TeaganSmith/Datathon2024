import pandas as pd
import matplotlib.pyplot as plt


# Load your dataset
data = pd.read_csv('combined_monarch_sightings.csv')  # Replace with your file path

# Group by year and calculate the total or average temperature
temp_by_year = data.groupby('year')['Temp_Mean'].agg(['sum', 'mean']).reset_index()

# Rename the columns
temp_by_year.columns = ['Year', 'Total_Temperature', 'Average_Temperature']
plt.figure(figsize=(10, 6))
plt.plot(temp_by_year['Year'], temp_by_year['Average_Temperature'], marker='o', color='b', label='Average Temperature')
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.title('Average Temperature by Year')
plt.grid(True)

plt.savefig('temp_plot.png', dpi=300, bbox_inches='tight')

temp_by_year = data.groupby('year')['AQI'].agg(['sum', 'mean']).reset_index()

# Rename the columns
temp_by_year.columns = ['Year', 'Total_Temperature', 'Average_Temperature']
plt.figure(figsize=(10, 6))
plt.plot(temp_by_year['Year'], temp_by_year['Average_Temperature'], marker='o', color='b', label='Average Temperature')
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.title('Average Temperature by Year')
plt.grid(True)

plt.savefig('aq_plot.png', dpi=300, bbox_inches='tight')
temp_by_year = data.groupby('year')['Count'].agg(['sum', 'mean']).reset_index()

# Rename the columns
temp_by_year.columns = ['Year', 'Total_Temperature', 'Average_Temperature']
plt.figure(figsize=(10, 6))
plt.plot(temp_by_year['Year'], temp_by_year['Average_Temperature'], marker='o', color='b', label='Average Temperature')
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.title('Average Temperature by Year')
plt.grid(True)

plt.savefig('butterfly_plot.png', dpi=300, bbox_inches='tight')
#plt.show()