import pandas as pd
import re

# Load data
data = pd.read_csv('customer_support_data.csv')

# Data cleaning function
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip().lower()

# Apply data cleaning
data['query'] = data['query'].apply(clean_text)
data['response'] = data['response'].apply(clean_text)

# Save cleaned data
data.to_csv('cleaned_customer_support_data.csv', index=False)
