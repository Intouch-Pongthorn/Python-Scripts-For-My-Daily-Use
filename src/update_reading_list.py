from bs4 import BeautifulSoup
import requests

url = input(r'enter url: ')
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
title = soup.title
print(title)