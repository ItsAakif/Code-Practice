import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the webpage you want to scrape
url = 'https://example.com'  # Replace with the URL of the website you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the text data you want from the webpage
    # For example, let's extract all the paragraphs
    paragraphs = [p.get_text() for p in soup.find_all('p')]

    # Create a dictionary to store the extracted data
    data = {
        'url': url,
        'text_data': paragraphs
    }

    # Define the name of the JSON file where you want to save the data
    json_file_name = 'web_data.json'

    # Write the data to a JSON file
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f'Data has been scraped and saved to {json_file_name}')
else:
    print('Failed to fetch the webpage.')

# <Web-Scraping> by Moutasim Qazi