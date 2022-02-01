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
    thelist = data_pull['items']
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
    with open("output2.csv", 'w') as csv_file:
        form.to_csv(csv_file)
    # csv_columns = ['imDbID','title', 'fullTitle','type', 'year', 'totalRating', 'totalRatingVotes', 'ratings',]

    # ------------------------------- PART 3 ------------------------------------------ #
    top1 = f"https://imdb-api.com/en/API/UserRatings/{secret.main()}/tt5491994"
    scrape = requests.get(top1)
    data01 = scrape.json()
    form01 = pd.DataFrame.from_dict(data01)
    top50 = f"https://imdb-api.com/en/API/UserRatings/{secret.main()}/tt0081834"
    scrape02 = requests.get(top50)
    data02 = scrape02.json()
    form02 = pd.DataFrame.from_dict(data02)
    top100 = f"https://imdb-api.com/en/API/UserRatings/{secret.main()}/tt4786824"
    scrape03 = requests.get(top100)
    data03 = scrape03.json()
    form03 = pd.DataFrame.from_dict(data03)
    top200 = f"https://imdb-api.com/en/API/UserRatings/{secret.main()}/tt2100976"
    scrape04 = requests.get(top200)
    data04 = scrape04.json()
    form04 = pd.DataFrame.from_dict(data04)

    with open("output3.csv", 'w') as fii:
        form01.to_csv(fii)
        fii.write("\n")
        form02.to_csv(fii)
        fii.write("\n")
        form03.to_csv(fii)
        fii.write("\n")
        form04.to_csv(fii)
        fii.write("\n")











main()
