import sqlite3
from typing import Tuple
import secrets
import requests
import pandas as pd
import csv


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS headline_data(
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        full_title TEXT NOT NULL,
        crew TEXT,
        year INTEGER NOT NULL,
        rating FLOAT DEFAULT 0,
        rating_count FLOAT DEFAULT 0);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings_data(
        id TEXT NOT NULL,
        Title TEXT NOT NULL,
        total_rating INTEGER NOT NULL,
        rating_votes TEXT NOT NULL,
        TenRateVotes INTEGER NOT NULL,
        TenRatingPercent FLOAT NOT NULL,
        NineRatingVotes INTEGER NOT NULL,
        NineRatingPercent INTEGER NOT NULL,
        EightRatingVotes FLOAT NOT NULL,
        EightRatePercent INTEGER NOT NULL,
        SevenRateVotes FLOAT NOT NULL,
        SevenRatePercent INTEGER NOT NULL,
        SixRatingVotes FLOAT NOT NULL,
        SixRatePercent INTEGER NOT NULL,
        FiveRatingVotes FLOAT NOT NULL,
        FiveRatePercent INTEGER NOT NULL,
        FourRatingVotes FLOAT NOT NULL,
        FourRatingPercent INTEGER NOT NULL,
        ThreeRatingVotes FLOAT NOT NULL,
        ThreeRatingPercent INTEGER NOT NULL,
        TwoRatingVotes FLOAT NOT NULL,
        TwoRatingPercent INTEGER NOT NULL,
        OneRatingVotes FLOAT NOT NULL,
        OneRatingPercent INTEGER NOT NULL,
        FOREIGN KEY (id) REFERENCES headline_data (id)
        ON DELETE CASCADE ON UPDATE NO ACTION);''')


url = f"https://imdb-api.com/en/API/Top250TVs/{secrets.API_KEY}"
results = requests.get(url)
data_pull = results.json()
thelist = data_pull['items']  # Takes only the pertinent info from the data scrape and appends to dictionary
keys = thelist[0].keys()  # Extracts the row/column headers for use in file (e.g: id, rating, etc. )
with open("output.csv", 'w') as f:
    dict_writer = csv.DictWriter(f, keys)  # Uses the dictionary writer of csv mod to write the row titles to file
    dict_writer.writeheader()  # Uses the csv python module to write the keys from dictionary to csv
    dict_writer.writerows(thelist)
    f.close()

loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.API_KEY}/tt7462410"
results = requests.get(loc)
data = results.json()
top1 = f"https://imdb-api.com/en/API/UserRatings/{secrets.API_KEY}/tt5491994"
results = requests.get(top1)
data_2 = results.json()
top50 = f"https://imdb-api.com/en/API/UserRatings/{secrets.API_KEY}/tt0081834"
results = requests.get(top50)
data_3 = results.json()
top100 = f"https://imdb-api.com/en/API/UserRatings/{secrets.API_KEY}/tt4786824"
results = requests.get(top100)
data_4 = results.json()
top200 = f"https://imdb-api.com/en/API/UserRatings/{secrets.API_KEY}/tt1492966"
results = requests.get(top200)
data_5 = results.json()


def flatten_dict(dictionary_with_list):
    flat_dict = {}
    flat_dict['imDbId'] = dictionary_with_list['imDbId']
    flat_dict['title'] = dictionary_with_list['title']
    flat_dict['totalRating'] = dictionary_with_list['totalRating']
    flat_dict['totalRatingVotes'] = dictionary_with_list['totalRatingVotes']
    for ratings_val in dictionary_with_list["ratings"]:
        new_key_base = f"rating {ratings_val['rating']}"
        new_votes_key = f"{new_key_base}_votes"
        flat_dict[new_votes_key] = ratings_val["votes"]
        percent_key = f"{new_key_base}_percent"
        flat_dict[percent_key] = ratings_val["percent"]
    return flat_dict


new_flat_version1 = flatten_dict(data)
new_flat_version2 = flatten_dict(data_2)
new_flat_version3 = flatten_dict(data_3)
new_flat_version4 = flatten_dict(data_4)
new_flat_version5 = flatten_dict(data_5)


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def get_data():
    top250 = pd.read_csv('output.csv', encoding="latin-1")
    return top250


def populate_headline_data(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    top250 = get_data()
    keys = top250['id'].tolist()
    data_dict = {}
    for item in keys:
        data_dict[item] = (top250.loc[top250['id'] == item]['title'].tolist()[0],
                           top250.loc[top250['id'] == item]['fullTitle'].tolist()[0],
                           top250.loc[top250['id'] == item]['crew'].tolist()[0],
                           top250.loc[top250['id'] == item]['year'].tolist()[0],
                           top250.loc[top250['id'] == item]['imDbRating'].tolist()[0],
                           top250.loc[top250['id'] == item]['imDbRatingCount'].tolist()[0])

    for key in data_dict.keys():
        cursor.execute("""INSERT INTO headline_data (id, title, full_title, crew, year, rating, rating_count)
                              VALUES (?,?,?,?,?,?,?)""", (key, data_dict[key][0], data_dict[key][1],
                                                          data_dict[key][2], data_dict[key][3], data_dict[key][4],
                                                          data_dict[key][5]))
        conn.commit()


l1 = list(new_flat_version1.items())
count = 0
l11 = []
while count < len(l1):
    l11.append(l1[count][1])
    count += 1

l2 = list(new_flat_version2.items())
count = 0
l22 = []
while count < len(l1):
    l22.append(l2[count][1])
    count += 1

l3 = list(new_flat_version3.items())
count = 0
l33 = []
while count < len(l1):
    l33.append(l3[count][1])
    count += 1

l4 = list(new_flat_version4.items())
count = 0
l44 = []
while count < len(l4):
    l44.append(l4[count][1])
    count += 1

l5 = list(new_flat_version5.items())
count = 0
l55 = []
while count < len(l5):
    l55.append(l5[count][1])
    count += 1


def populate_ratings_data(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.executemany('''INSERT INTO ratings_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (l11,))
    conn.commit()
    cursor.executemany('''INSERT INTO ratings_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (l22,))
    conn.commit()
    cursor.executemany('''INSERT INTO ratings_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', (l33,))
    conn.commit()
    cursor.executemany('''INSERT INTO ratings_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', (l44,))
    conn.commit()
    cursor.executemany('''INSERT INTO ratings_data VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', (l55,))
    conn.commit()


def main():
    name = 'movie_api.db'
    conn, cursor = open_db(name)
    setup_db(cursor)
    populate_ratings_data(cursor, conn)
    populate_headline_data(cursor, conn)
    conn.commit()
    close_db(conn)


main()
