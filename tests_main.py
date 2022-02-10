import requests
import secrets


def data_scrape():
    url = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(url)
    data_pull = results.json()
    the_list = data_pull['items']  # Takes only the pertinent info from the data scrape and appends to dictionary
    return len(the_list)
