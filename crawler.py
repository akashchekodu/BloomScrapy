from bloom_filter import BloomFilter
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse



class WebCrawlerWithBloomFilter:
    def __init__(self,seed_url,max_urls=100,bloom_filter_size=100,num_hashes=5):
        self.seed_url = seed_url
        self.bloom_filter = BloomFilter(size=bloom_filter_size,num_hashes=num_hashes)
        self.max_urls = max_urls
        self.visited_count = 0
    
    def is_same_domain(self,base_url,target_url):
        # Ensure we stay within the same domain
        return urlparse(base_url).netloc == urlparse(target_url).netloc
    
    def fetch_and_parse(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except (requests.RequestException, ValueError):
            print(f"Failed to fetch {url}")
            return None
    
    def extract_links(self, soup, base_url):
        links = set()
        for link_tag in soup.find_all('a', href=True):
            absolute_url = urljoin(base_url, link_tag['href'])
            # Filter to keep URLs within the same domain only
            if self.is_same_domain(base_url, absolute_url):
                links.add(absolute_url)
        return links
    

    def crawl(self):
        to_visit = {self.seed_url}

        while to_visit and self.visited_count < self.max_urls:
            url = to_visit.pop()

            if self.bloom_filter.contains(url):
                continue  # Skip if already visited

            soup = self.fetch_and_parse(url)
            if soup is None:
                continue  # Skip if failed to fetch

            print(f"Crawling: {url}")
            self.visited_count += 1
            self.bloom_filter.add(url)

            new_links = self.extract_links(soup, url)
            to_visit.update(new_links - {url for url in new_links if self.bloom_filter.contains(url)})

            time.sleep(1)


if __name__ == "__main__":
    seed_url = "https://moneycontrol.com"
    crawler = WebCrawlerWithBloomFilter(seed_url=seed_url, max_urls=100)
    crawler.crawl()
