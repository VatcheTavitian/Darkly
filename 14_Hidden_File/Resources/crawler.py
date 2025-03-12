import requests


from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, urljoin

# Define the base URL
base_url = "http://10.18.125.219:8000/.hidden/"

# Define the domains to exclude
exclude_domains = ['wikipedia.org', 'facebook.com', 'instagram.com', 'twitter.com', 'x.com', 'page=']

# Function to check if the URL is from an excluded domain
def is_excluded(url):
    parsed_url = urlparse(url)
    for domain in exclude_domains:
        if domain in parsed_url.netloc:
            return True
    return False

# Function to crawl the website
def crawl(url, depth=6, visited=None):
    if visited is None:
        visited = set()
    # print(url)
    # Avoid re-crawling the same URL
    if url in visited or depth < 0:
        return []

    visited.add(url)
    urls_to_scrape = []
    
    # Send a request to the URL
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all links from the page
    links = soup.find_all('a', href=True)
    
    for link in links:
        href = link['href']
        full_url = urljoin(url, href)
        
        # If the link is not excluded, add it to the list
        if not is_excluded(full_url):
            urls_to_scrape.append(full_url)
            # Recursively crawl the next level with reduced depth
            urls_to_scrape.extend(crawl(full_url, depth-1, visited))
    
    return urls_to_scrape

# Crawl starting from the base URL
scraped_urls = crawl(base_url)

# Write the result to a JSON file
output_filename = "scraped_urls.json"
with open(output_filename, "w") as outfile:
    json.dump(scraped_urls, outfile, indent=4)

print(f"Crawling complete. Results saved to {output_filename}")