# Start to my IMDB Project
import csv
import sys
import requests
import secret
from time import sleep
from urllib.request import Request, urlopen
import pandas as pd


def main():
    # ------------------------------ Part I Start ------------------------------- #
    original_stdout = sys.stdout
    url = f"https://imdb-api.com/en/API/Top250TVs/{secret.main()}"
    results = requests.get(url)

    if results.status_code != 200:
        print("Uh-Oh")
        return
    data_pull = results.json()
    # print(str(data_pull))
    thelist = data_pull['items']
    # print(list)
    keys = thelist[0].keys()
    with open("output.csv", 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(thelist)
        f.close()

    # -------------------------------- PART 2 -------------------------------------- #

    loc = f"https://imdb-api.com/en/API/UserRatings/{secret.main()}/tt7462410"
    res_2 = requests.get(loc)
    data_2 = res_2.json()
    form = pd.DataFrame.from_dict(data_2)
    # print(data_2)
    with open("output2.csv",'w') as csv_file:
        form.to_csv(csv_file)
    # csv_columns = ['imDbID','title', 'fullTitle','type', 'year', 'totalRating', 'totalRatingVotes', 'ratings',]






main()
