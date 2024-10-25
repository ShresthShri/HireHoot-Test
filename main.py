# main.py

import pandas as pd
from cleaner import clean_text  # Import the cleaning function
from preprocess import preprocess_text  # Import the preprocessing function

# Load your CSV data
data = pd.read_csv(r'data/nyc-jobs-1.csv', encoding='utf-8-sig')

# Selecting the relevant columns to preprocess
text_columns = ['Job Description', 'Minimum Qual Requirements', 'Preferred Skills']

# Preprocess each text column
for col in text_columns:
    # Create new DataFrame columns for the processed results
    processed_results = data[col].dropna().apply(lambda x: pd.Series(preprocess_text(str(x))))
    
    # Define new column names for the processed data
    new_column_names = [f'{col}_filtered', f'{col}_stemmed', f'{col}_lemmatized', f'{col}_original']
    
    # Set processed result columns
    processed_results.columns = new_column_names
    
    # Merge processed results back into the main DataFrame, matching indices
    data[new_column_names] = processed_results.reindex(data.index, fill_value='')

# Optionally, save the processed DataFrame to a new CSV file
data.to_csv('processed_nyc_jobs.csv', index=False)

# Clean the data as well
clean_text(data)

# Print the DataFrame to check the results
print(data.head())
