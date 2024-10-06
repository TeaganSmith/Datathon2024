import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Function to perform Negative Binomial Regression
def negative_binomial_regression(data_file):
    """
    This function reads a CSV file, performs a Negative Binomial Regression 
    on the 'Count' variable using predictors such as 'Temp_Mean', 'AQI', and 'season', 
    and prints the regression summary.
    
    Parameters:
    data_file (str): The path to the CSV file containing the data.
    """
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(data_file)
    
    # Check the data columns to make sure they are as expected
    print("Data columns:", data.columns)
    
    # Fit the Negative Binomial model
    # Example predictors: Temp_Mean (mean temperature), AQI (Air Quality Index), and season
    # You can adjust the formula to include other predictors if necessary
    formula = 'Count ~ Temp_Mean + AQI + year + season'
    
    # Fitting the Negative Binomial model
    nb_model = smf.glm(formula, data=data, family=sm.families.NegativeBinomial()).fit()

    # Print the model summary
    print(nb_model.summary())

# Example usage: Replace 'your_data_file.csv' with the path to your actual data file
data_file = 'extra-csvs/combined_monarch_sightings_filled.csv'
negative_binomial_regression(data_file)