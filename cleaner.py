import re

def clean_text(data):
    # Need to clean the data to specify the skills, experience and job title only

    # Define a list of special words you want to remove
    special_words = ['â', '€', '¢']

    # Join the special words into a regex pattern (case-insensitive)
    pattern = '|'.join([re.escape(word) for word in special_words])

    # Clean the special words from a string
    def clean_text(text):
        if isinstance(text, str):
            return re.sub(pattern, '', text, flags=re.IGNORECASE)
        return text

    # Apply the function to all columns in the DataFrame
    data_cleaned = data.applymap(clean_text)

    # Save the cleaned data back to the CSV File
    data_cleaned.to_csv('Cleaned_data.csv', index = False)

    print("Data Cleaned and saved")
    #print(data.head())
