import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, urljoin


base_url = "http://localhost:8000/.hidden/"


exclude_domains = ['wikipedia.org', 'facebook.com', 'instagram.com', 'twitter.com']


def is_excluded(url):
    parsed_url = urlparse(url)
    for domain in exclude_domains:
        if domain in parsed_url.netloc:
            return True
    return False


def crawl(url, depth=3, visited=None):
    if visited is None:
        visited = set()


    if url in visited or depth < 0:
        return []

    visited.add(url)
    urls_to_scrape = []
    

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

   
    soup = BeautifulSoup(response.content, 'html.parser')
    
 
    links = soup.find_all('a', href=True)
    
    for link in links:
        href = link['href']
        full_url = urljoin(url, href)
        
       
        if not is_excluded(full_url):
            urls_to_scrape.append(full_url)
            urls_to_scrape.extend(crawl(full_url, depth-1, visited))
    
    return urls_to_scrape


scraped_urls = crawl(base_url)

output_filename = "scraped_urls.json"
with open(output_filename, "w") as outfile:
    json.dump(scraped_urls, outfile, indent=4)

print(f"Crawling complete. Results saved to {output_filename}")

