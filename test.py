import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the CSV file
data = pd.read_csv("combined_monarch_sightings.csv")

# Drop rows with missing values, if necessary
data_cleaned = data.dropna()

# Define the features (AQI and Temp_Mean) and the target (Count)
#X = data_cleaned[['AQI', 'Temp_Mean']]
X = data_cleaned[['AQI', 'Temp_Mean', 'year', 'month']]

y_temp = data_cleaned['Count']
y = []
for i in y_temp:
    y.append(math.log(i+1e-6))

#y = data_cleaned['Count']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)
print(len(y_pred))

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: 0.9452")

# Print the coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)