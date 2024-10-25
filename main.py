# main.py

import pandas as pd
# from cleaner import clean_text  # Import the cleaning function
from preprocess import preprocess_text  # Import the preprocessing function

# Load your CSV data
data = pd.read_csv(r'data/nyc-jobs-1.csv', encoding='utf-8')

# Selecting the relevant columns to preprocess
text_columns = ['Job Description', 'Minimum Qual Requirements', 'Preferred Skills']

# Preprocess each text column and store only the lemmatized results
for col in text_columns:
    # Extract only lemmatized words from the preprocessing function
    lemmatized_results = data[col].dropna().apply(lambda x: preprocess_text(str(x))[2])  # [2] for lemmatized words

    # Assign the lemmatized results to a new column in the main DataFrame
    data[f'{col}_lemmatized'] = lemmatized_results.reindex(data.index, fill_value='')

# Filter the DataFrame to include only the lemmatized columns
lemmatized_columns = [f'{col}_lemmatized' for col in text_columns]
lemmatized_data = data[lemmatized_columns]

# Optionally, save the lemmatized DataFrame to a new CSV file
lemmatized_data.to_csv('processed_nyc_jobs_lemmatized.csv', index=False)

# Print the lemmatized DataFrame to check the results
print(lemmatized_data.head())

