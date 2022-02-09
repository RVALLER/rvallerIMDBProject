# Start to my IMDB Project
import csv

import requests
import secret
import pandas as pd


def extract():
    # ------------------------------ Part I Start ------------------------------- #
    url = f"https://imdb-api.com/en/API/Top250TVs/{secret.main()}"
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
    # -------------------------------- PART 2 -------------------------------------- #

    loc = f"https://imdb-api.com/en/API/UserRatings/{secret.main()}/tt7462410"
    res_2 = requests.get(loc)
    data_2 = res_2.json()
    form = pd.DataFrame.from_dict(data_2)  # Creates a dataframe in pandas to extract a single api scrape for csv output
    with open("output2.csv", 'w') as csv_file:
        form.to_csv(csv_file)  # uses to_csv to convert dataframe to the csv file in proper formatting
    # ------------------------------- PART 3 ------------------------------------------ #

    # This portion of code uses similar pieces from part I and II and siphons relevant data
    # from top 1, 50, 150, and 200 and appends it to the section below Part I's write.
    # top1, top50, top100 and top200 are variables to store api data for ratings
    # forms01-04 are for dataframing the apis and scrapes01-04 are simply to fetch request the data

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
    top200 = f"https://imdb-api.com/en/API/UserRatings/{secret.main()}/tt1492966"
    scrape04 = requests.get(top200)
    data04 = scrape04.json()
    form04 = pd.DataFrame.from_dict(data04)

    # Final comments: the new lines are just for less of an eyesore for the output

    with open("output2.csv", 'a') as fii:
        fii.write("\n\n\n\n\n")
        form01.to_csv(fii)
        fii.write("\n")
        form02.to_csv(fii)
        fii.write("\n")
        form03.to_csv(fii)
        fii.write("\n")
        form04.to_csv(fii)
        fii.write("\n")


    # ----------------------------------- Database Portion for Sprint 2 ------------------------
    # flat_dict = {}
    # list(flat_dict) = data01
    # for i in data01['ratings']:
    #     data01.append(i)
    #
    # print(flat_dict)
    #
    # for item in flat_dict:
    #     rate = item["rating"]
    #     ratekey = f"{rate}rating"
    #     percentKey = f"{rate}percent"
    #     flat_dict[percentKey] = item["percent"]
    #
    # print(flat_dict)

    sample_dict = {"class": "comp490",
                   "cap": 24,
                   "outcomes": [
                       {"number": 1,
                        "name": "work in groups",
                        "origen": "alumni"},
                       {"number": 2,
                        "name": "Ethical Dilemmas",
                        "origen": "Local Hiring Managers"}
                   ]}

    def flatten_dict(dictionary_with_list):
        flat_dict = {}
        flat_dict['class'] = dictionary_with_list['class']
        flat_dict['cap'] = dictionary_with_list['cap']
        for outcome_val in dictionary_with_list["outcomes"]:
            new_key_base = f"outcome {outcome_val['number']}"
            name_key = f"{new_key_base}_name"
            flat_dict[name_key] = outcome_val["name"]
            origen_key = f"{new_key_base}_origen"
            flat_dict[origen_key] = outcome_val["origen"]
        return flat_dict

    def main():
        new_flat_version = flatten_dict(sample_dict)
        print(new_flat_version)

    if __name__ == '__main__':
        main()


extract()

'''
take his code api apply in function for adding data for rankings
seperate functions for eac h id (ttcode)
for key, value in data
    if key == 'id'
        value = name
insert values(?, ?, ?, ?) , (name...)"""
insert
'''
