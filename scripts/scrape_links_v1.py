import requests
from bs4 import BeautifulSoup
import json

def get_all_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except requests.RequestException as e:
        print(f"Error: {e}")
        return []

#return all links from bmsce.ac.in domain
def crawl_website(starting_url, depth=3):
    visited_urls = set()
    bmsce_urls = []

    def crawl(url, current_depth):
        if current_depth > depth:
            return
        if url in visited_urls:
            return

        visited_urls.add(url)
        #check if url contains bmsce.ac.in
        if "bmsce.ac.in" in url:
            bmsce_urls.append(url)
        # print(f"Crawling: {url}")
        

        links = get_all_links(url)
        for link in links:
            crawl(link, current_depth + 1)

    crawl(starting_url, 1)
    return bmsce_urls



#scrape all links from a list
def scrape_links(links_list):
    data = []

    for link in links_list:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = ' '.join([p.get_text() for p in soup.find_all('p')])  # Extract text from paragraphs, adjust as needed

        metadata = {
            'link': link,
            'title': soup.title.text if soup.title else None,  # Extract title if available
        }

        entry = {
            'metadata': metadata,
            'text': text,
        }

        data.append(entry)

    return data

def save_to_json(data, filename='output.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    starting_url = 'https://bmsce.ac.in'
    bmsce_urls = crawl_website(starting_url)
    print(len(bmsce_urls))
    scraped_data = scrape_links(bmsce_urls)
    save_to_json(scraped_data, 'bmsce_website_text.json')