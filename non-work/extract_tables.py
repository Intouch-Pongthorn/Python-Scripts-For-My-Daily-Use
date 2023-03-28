import pandas as pd
from sys import argv as arg

def main():
    url = "path"
    data_frame = pd.read_html(url)
    data_frame.to_csv(r"path")