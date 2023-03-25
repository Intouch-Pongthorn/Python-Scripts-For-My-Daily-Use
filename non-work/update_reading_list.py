#!/usr/bin/env python
import os
from sys import argv 
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()
location_path = os.getenv("READING_LIST_DIR_LOCATION")

def main():
    url =  argv[1]
    title =  get_title(url)
    write_note(title,url)
    
    
def get_title(url:str)->str:
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    title = soup.title.text
    return title

def write_note(title:str,url:str)->None:
    #opens the text file in from the location.if the file doesn't exist,it'll be automatically created.
    with open(location_path,"a") as file:
        file.write("\n")
        file.write(f"title: {title} ")
        file.write("\n")
        file.write(f"url: {url} ")
        file.write("\n")
        file.write("#"*30)
        file.write("\n")

if __name__ == "__main__":
    main()