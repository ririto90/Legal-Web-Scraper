import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
import re
import os

# Function to extract content from a URL
def get_text_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract text from the page
            text = soup.get_text(separator=' ')
            return text
        else:
            print(f"Failed to fetch URL: {url}")
            return None
    except Exception as e:
        print(f"Error fetching URL {url}: {str(e)}")
        return None

# Function to clean and split text into words
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    words = re.findall(r'\b\w+\b', text.lower())  # Extract words
    return words

# Function to search for keyword occurrences in the text from the URL
def search_keywords_in_url(url, keywords):
    text = get_text_from_url(url)
    if text:
        words = clean_text(text)
        word_count = Counter(words)
        # Filter only the relevant keywords
        return {word: word_count[word] for word in keywords if word in word_count}
    return {}

# Define the list of URLs and keywords to search
urls = [
    'https://boe.es/boe/dias/2007/12/03/',
    'https://boe.es/boe/dias/2007/12/04/',
    # Add more URLs as needed
]

keywords = ["law", "legal", "court", "rights"]  # Add your own list of keywords

# Prepare the output data
data_rows = []
for url in urls:
    keyword_counts = search_keywords_in_url(url, keywords)
    row = [url] + [keyword_counts.get(word, 0) for word in keywords]
    data_rows.append(row)

# Create a DataFrame
df = pd.DataFrame(data_rows, columns=["URL"] + keywords)

# Save the DataFrame to an Excel file
output_file = 'URL_Keyword_Search.xlsx'
df.to_excel(output_file, index=False)

print(f"Data saved to {output_file}")
