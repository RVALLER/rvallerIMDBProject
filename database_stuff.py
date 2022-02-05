import sqlite3
from typing import Tuple
import secret
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
        total_rating FLOAT NOT NULL,
        rating_votes INTEGER NOT NULL,
        TenRating FLOAT NOT NULL,
        TenRateVotes INTEGER NOT NULL,
        NineRating FLOAT NOT NULL,
        NineRateVotes INTEGER NOT NULL,
        EightRating FLOAT NOT NULL,
        EightRateVotes INTEGER NOT NULL,
        SevenRate FLOAT NOT NULL,
        SevenRateVotes INTEGER NOT NULL,
        SixRating FLOAT NOT NULL,
        SixRateVotes INTEGER NOT NULL,
        FiveRating FLOAT NOT NULL,
        FiveRateVotes INTEGER NOT NULL,
        FourRate FLOAT NOT NULL,
        FourRateVotes INTEGER NOT NULL,
        ThreeRate FLOAT NOT NULL,
        ThreeRateVotes INTEGER NOT NULL,
        TwoRate FLOAT NOT NULL,
        TwoRateVotes INTEGER NOT NULL,
        OneRate FLOAT NOT NULL,
        OneRateVotes INTEGER NOT NULL,
        FOREIGN KEY (id) REFERENCES headline_data (id)
        ON DELETE CASCADE ON UPDATE NO ACTION);''')


url = f"https://imdb-api.com/en/API/Top250TVs/{secret.main()}"
results = requests.get(url)
data_pull = results.json()
thelist = data_pull['items']  # Takes only the pertinent info from the data scrape and appends to dictionary
keys = thelist[0].keys()  # Extracts the row/column headers for use in file (e.g: id, rating, etc. )
with open("output.csv", 'w') as f:
    dict_writer = csv.DictWriter(f, keys)  # Uses the dictionary writer of csv mod to write the row titles to file
    dict_writer.writeheader()  # Uses the csv python module to write the keys from dictionary to csv
    dict_writer.writerows(thelist)
    f.close()

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

def get_rate():
    r_data = pd.read_cvs('output2.csv', encoding="latin-1")
    return r_data

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

# def populate_ratings_data(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
#     r_data = get_rate()
#     keyz = r_data[]

def main():
    name = 'movie_api.db'
    conn, cursor = open_db(name)
    setup_db(cursor)
    populate_headline_data(cursor, conn)
    conn.commit()
    close_db(conn)


main()
