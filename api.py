import csv

import requests
import secrets
import pandas as pd
from operator import itemgetter
# test comment to check workflow

loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt7462410"
results = requests.get(loc)
data = results.json()
top1 = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt5491994"
results = requests.get(top1)
data_2 = results.json()
top50 = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt0081834"
results = requests.get(top50)
data_3 = results.json()
top100 = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt4786824"
results = requests.get(top100)
data_4 = results.json()
top200 = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt1492966"
results = requests.get(top200)
data_5 = results.json()

def flatten_dict(dictionary_with_list):
    flat_dict = {}
    flat_dict['imDbId'] = dictionary_with_list['imDbId']
    flat_dict['title']= dictionary_with_list['title']
    flat_dict['totalRating']= dictionary_with_list['totalRating']
    flat_dict['totalRatingVotes']= dictionary_with_list['totalRatingVotes']
    for ratings_val in dictionary_with_list["ratings"]:
        new_key_base = f"rating {ratings_val['rating']}"
        new_votes_key = f"{new_key_base}_votes"
        flat_dict[new_votes_key]=ratings_val["votes"]
        percent_key = f"{new_key_base}_percent"
        flat_dict[percent_key] = ratings_val["percent"]
    return flat_dict

def main():
    new_flat_version1 = flatten_dict(data)
    new_flat_version2 = flatten_dict(data_2)
    new_flat_version3 = flatten_dict(data_3)
    new_flat_version4 = flatten_dict(data_4)
    new_flat_version5 = flatten_dict(data_5)
    print(new_flat_version5)

if __name__ == '__main__':
    main()
