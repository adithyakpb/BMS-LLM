import requests
from bs4 import BeautifulSoup
import json
from langchain.document_loaders import SeleniumURLLoader

#use selenium to get text data from a webpage
def get_text_data(url):
    loader = SeleniumURLLoader(urls = [url])
    document = loader.load()
    metadata = document[0].metadata
    text = document[0].page_content
    return metadata, text

if __name__ == "__main__":
    url = "https://bmsce.ac.in"
    metadata, text = get_text_data(url)
    print(metadata)
    # print(text)


# function to extract ALL content from a webpage, use langchain if required
# def extract_content(url):
#     try:
#         # Fetch the webpage content
#         response = requests.get(url)
#         if response.status_code == 200:
#             print(f"Successfully fetched the webpage from {url}")
#             # Parse the HTML content using BeautifulSoup
#             soup = BeautifulSoup(response.text, 'html.parser')
#             # Extract the main content of the webpage
#             main_content = soup.find('body').text
#         else:
#             print(f"Failed to fetch the webpage. Status code: {response.status_code}")
#             main_content = ""
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         main_content = ""
#     return main_content