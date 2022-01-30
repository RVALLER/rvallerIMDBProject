# Start to my IMDB Project
import csv
import sys
import requests
import secret
from bs4 import BeautifulSoup
import _pickle as cPickle
import json
import pandas as pd


def main():
    # Save Reference
    original_stdout = sys.stdout
    url = f"https://imdb-api.com/en/API/Top250TVs/{secret.main()}"
    results = requests.get(url)

    if results.status_code != 200:
        print("Uh-Oh")
        return
    data_pull = results.json()
   # print(str(data_pull))
    thelist=data_pull['items']
    # print(list)
    keys = thelist[0].keys()
    with open("output.csv", 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(thelist)
        f.close()


main()
