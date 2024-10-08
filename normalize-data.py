import pandas as pd

def min_max_normalize(df, column):
    """
    Apply Min-Max normalization to a specific column in the dataframe.
    
    Parameters:
    df (pd.DataFrame): The input dataframe
    column (str): The column to normalize
    
    Returns:
    pd.DataFrame: The dataframe with the normalized column
    """
    df[f'{column}_Normalized'] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df

def normalize_csv(input_csv, output_csv):
    """
    Load a CSV file, normalize the 'Count' column, and save the result to a new CSV file.
    
    Parameters:
    input_csv (str): Path to the input CSV file
    output_csv (str): Path to save the output CSV file
    """
    # Load the CSV file into a DataFrame
    year = 2022
    df = pd.read_csv(input_csv)
    
    # Apply Min-Max normalization to the 'Count' column
    df = min_max_normalize(df, 'Count')
    
    # Save the resulting DataFrame to a new CSV file
    df.to_csv(output_csv, index=False)
    print(f'Normalized data saved to {output_csv}')

# Example usage
input_csv = 'csv-files-data/2021/monarch_sightings2021_with_fips.csv'  # Replace with your actual input file path
output_csv = 'csv-files-data/2021/normalized_monarch_sightings2021.csv'  # Replace with your desired output file path

normalize_csv(input_csv, output_csv)
