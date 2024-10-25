# preprocess.py
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary NLTK data (run once)
if not nltk.data.path:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')    

# Define the preprocessing function
def preprocess_text(text):

    if not text or not isinstance(text, str):  # Handle non-string input
        return [], [], [], ""  # Return empty lists and an empty string

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters using regex
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Replace non-ASCII characters with a space

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Stemming
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_tokens]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens if word.isalpha()]


    return filtered_tokens, stemmed_words, lemmatized_words, text
