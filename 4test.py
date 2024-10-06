import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")

# Load the CSV file
data = pd.read_csv("combined_monarch_sightings_filled.csv")

# Filter the data for the months of August (8) to November (11)
data_filtered = data[(data['month'] >= 8) & (data['month'] <= 11)]

# Drop rows with missing values
data_cleaned = data_filtered.dropna()

# Define the features (AQI, Temp_Mean, year, month, and day) and the target (Count)
X = data_cleaned[['AQI', 'Temp_Mean', 'year', 'month', 'day']]
y = data_cleaned['Count']

# Check feature correlations
print("Feature Correlations with Count:")
print(data_cleaned[['AQI', 'Temp_Mean', 'year', 'month', 'day', 'Count']].corr())

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model
print("\n--- Linear Regression ---")
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Polynomial Features Model
print("\n--- Polynomial Regression ---")
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
X_train_poly, X_test_poly, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)
model.fit(X_train_poly, y_train)
y_pred_poly = model.predict(X_test_poly)
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)
print(f"Mean Squared Error (Polynomial): {mse_poly}")
print(f"R^2 Score (Polynomial): {r2_poly}")

# Random Forest Model
# Log Transformation of the Target

# Visualization: Temperature, AQI, and Count by day of the month

# Plot 1: Temp_Mean by day of the month (August to November)
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['day'], data_cleaned['Temp_Mean'], marker='o', linestyle='-', color='r')
plt.title('Temperature (Mean) by Day of the Month (Aug to Nov 2021)')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.savefig("temperature_by_day_aug_nov.png")
plt.show()

# Plot 2: AQI by day of the month (August to November)
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['day'], data_cleaned['AQI'], marker='o', linestyle='-', color='b')
plt.title('AQI by Day of the Month (Aug to Nov 2021)')
plt.xlabel('Day of the Month')
plt.ylabel('Air Quality Index')
plt.grid(True)
plt.savefig("aqi_by_day_aug_nov.png")
plt.show()

# Plot 3: Monarch Butterfly Count by day of the month (August to November)
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned['day'], data_cleaned['Count'], marker='o', linestyle='-', color='g')
plt.title('Monarch Butterfly Count by Day of the Month (Aug to Nov 2021)')
plt.xlabel('Day of the Month')
plt.ylabel('Butterfly Count')
plt.grid(True)
plt.savefig("count_by_day_aug_nov.png")
plt.show()
