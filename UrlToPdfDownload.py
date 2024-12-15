from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession



URL = input('Web Site Link: ')
FILETYPE = '.pdf'

def get_soup(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')


print(get_soup(URL).find_all('a'))

for link in get_soup(URL).find_all('a'):
    file_link = link.get('href')
    if FILETYPE in file_link:
        file_name = file_link.split('/')[-1]
        print(file_name)
        with open(file_name, 'wb') as file:
            response = requests.get(file_link)
            file.write(response.content)