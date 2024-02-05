import requests
import json
from bs4 import BeautifulSoup

def extract_links_from_sitemap(sitemap_url):
    links = []
    try:
        # Fetch the sitemap content
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            print(f"Successfully fetched the sitemap from {sitemap_url}")
            # Parse the XML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <a> tags
            a_tags = soup.find_all('a')

            # Extract and print the href attribute from each <a> tag
            for a_tag in a_tags:
                links.append(a_tag.get('href'))
                
        else:
            print(f"Failed to fetch the sitemap. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return links



if __name__ == "__main__":
    all_links = []
    sitemap_url = 'https://bmsce.ac.in/home/sitemap'
    links = extract_links_from_sitemap(sitemap_url)
    all_links.extend(links)
    for link in links:
        new_links = extract_links_from_sitemap(link)
        for new_link in new_links:
            if new_link not in all_links:
                all_links.append(new_link)
    with open('bmsce_links.json', 'w') as f:
        json.dump(all_links, f, indent=4)