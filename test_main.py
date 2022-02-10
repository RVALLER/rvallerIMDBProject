import requests
from typing import Tuple

import secret
import sqlite3

import secrets


def extract():
    # ------------------------------ Part I Start ------------------------------- #
    url = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(url)

    if results.status_code != 200:
        print("Uh-Oh")
        return
    data_pull = results.json()
    thelist = data_pull['items']  # Takes only the pertinent info from the data scrape and appends to dictionary
    return thelist


extract()
