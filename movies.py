# Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of URLs to scrape
urls = [
    "https://www.imdb.com/title/tt15398776/",
    "https://www.imdb.com/title/tt9362722",
    "https://www.imdb.com/title/tt15239678",
    "https://www.imdb.com/title/tt29623480",
    "https://www.imdb.com/title/tt1745960"
]

# Define headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# List to store the data
data = []

# Loop through each URL with an index
for i, url in enumerate(urls, start=1):
    print(f"Processing {i} of {len(urls)}")
    
    # Send an HTTP request to fetch the page content
    response = requests.get(url, headers=headers)

    # Raise exception if request was unsuccessful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve data from {url}. \nStatus code: {response.status_code}, \nError: {response.text}")
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title_tag = soup.find('span', {'class': 'hero__primary-text', 'data-testid': 'hero__primary-text'})
    title = title_tag.text.strip() if title_tag else 'Title Not Found'

    # Extract rating
    rating_tag = soup.find('span', {'class': 'sc-d541859f-1', 'class': 'imUuxf'})
    rating = rating_tag.text.strip() if rating_tag else 'Rating Not Found'

    # Extract story (plot summary)
    plot_tag = soup.find('span', {'role': 'presentation', 'data-testid': 'plot-xl', 'class': 'sc-3ac15c8d-2'})
    plot = plot_tag.text.strip() if plot_tag else 'Plot Not Found'

    # Append the extracted data to the list
    data.append({
        "URL": url,
        "Title": title,
        "Rating": rating,
        "Story": plot
    })

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Optionally, save the data to a CSV file
df.to_csv('imdb_movie_data.csv', index=False)