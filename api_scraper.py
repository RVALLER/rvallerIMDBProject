# Start to my IMDB Project
import csv
import requests
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


def output():
    url = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(url)

    if results.status_code != 200:
        print("Uh-Oh")
        return
    data_pull = results.json()
    thelist = data_pull['items']  # Takes only the pertinent info from the data scrape and appends to dictionary
    keys = thelist[0].keys()  # Extracts the row/column headers for use in file (e.g: id, rating, etc. )
    with open("output.csv", 'w') as f:
        dict_writer = csv.DictWriter(f, keys)  # Uses the dictionary writer of csv mod to write the row titles to file
        dict_writer.writeheader()  # Uses the csv python module to write the keys from dictionary to csv
        dict_writer.writerows(thelist)
        f.close()


output()
'''
take his code api apply in function for adding data for rankings
seperate functions for eac h id (ttcode)
for key, value in data
    if key == 'id'
        value = name
insert values(?, ?, ?, ?) , (name...)"""
insert
'''
