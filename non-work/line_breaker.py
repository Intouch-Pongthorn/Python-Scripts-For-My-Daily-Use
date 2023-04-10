#!/usr/bin/env python
from sys import argv as arg

def main():
    text = str(arg[1])
    seperator = str(arg[2])
    line_breaker(text,seperator)

def line_breaker(text:str,seperator:str):
    text_list = [f"{seperator}{sub_text}"for sub_text in text.split(seperator)]
    for member in text_list:
        print(member)

if __name__ == "__main__":
    main()