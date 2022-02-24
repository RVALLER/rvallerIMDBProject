import secrets
import requests
import sqlite3
import pandas as pd
import csv
from typing import Tuple
import database_stuff


loc = f"https://imdb-api.com/en/API/MostPopularTVs/{secrets.API_KEY}"
res = requests.get(loc)
data01 = res.json()
dlist = data01['items']

loc_2 = f"https://imdb-api.com/en/API/Top250Movies/{secrets.API_KEY}"
res_2 = requests.get(loc_2)
data02 = res_2.json()
dlist02 = data02['items']
keyz = dlist02[0].keys()  # Extracts the row/column headers for use in file (e.g: id, rating, etc. )

loc_3 = f"https://imdb-api.com/en/API/MostPopularMovies/{secrets.API_KEY}"
res_3 = requests.get(loc_3)
data03 = res_3.json()
dlist03 = data03['items']
ki = dlist03[0].keys()

with open("output2.csv", 'w') as f:
    dict_writer = csv.DictWriter(f, keyz)  # Uses the dictionary writer of csv mod to write the row titles to file
    dict_writer.writeheader()  # Uses the csv python module to write the keys from dictionary to csv
    dict_writer.writerows(dlist02)
    f.close()

with open("output3.csv", 'w') as f:
    dict_writer = csv.DictWriter(f, ki)  # Uses the dictionary writer of csv mod to write the row titles to file
    dict_writer.writeheader()  # Uses the csv python module to write the keys from dictionary to csv
    dict_writer.writerows(dlist03)
    f.close()


def db_setter(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS pop_shows(
        id TEXT PRIMARY KEY,
        rank TEXT,
        rankUpDown FLOAT,
        title TEXT,
        fullTitle INTEGER,
        year FLOAT DEFAULT 0,
        crew TEXT,
        imDbRating TEXT,
        imDbRatingCount FLOAT DEFAULT 0);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS movie_headlines(
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            full_title TEXT NOT NULL,
            crew TEXT,
            year INTEGER NOT NULL,
            rating FLOAT DEFAULT 0,
            rating_count FLOAT DEFAULT 0);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS movie_upDownTrend(
            id TEXT PRIMARY KEY,
            title TEXT
            full_title TEXT
            imDbRating
            imDbRatingCount FLOAT DEFAULT 0,
            rankUpDown FLOAT DEFAULT 0);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS pop_movies(
            id TEXT PRIMARY KEY,
            rank TEXT,
            rankUpDown FLOAT,
            title TEXT,
            fullTitle INTEGER,
            year FLOAT DEFAULT 0,
            crew TEXT,
            imDbRating TEXT,
            imDbRatingCount FLOAT DEFAULT 0,
            FOREIGN KEY (id) REFERENCES movie_headlines (id)
            ON DELETE CASCADE ON UPDATE NO ACTION);''')


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def pop_csv():
    with open("output.csv", 'w') as f:
        keys = dlist[0].keys()
        dict_writer = csv.DictWriter(f, keys)  # Uses the dictionary writer of csv mod to write the row titles to file
        dict_writer.writeheader()  # Uses the csv python module to write the keys from dictionary to csv
        dict_writer.writerows(dlist)
        f.close()


def get_data():
    mostpop = pd.read_csv('output.csv', encoding="latin-1")
    return mostpop


def get_movies():
    top250_movies = pd.read_csv('output2.csv', encoding="latin-1")
    return top250_movies


def get_data03():
    pop_movies = pd.read_csv('output3.csv', encoding="latin-1")
    return pop_movies


def populate_pop_shows(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    head_d = get_data()
    key = head_d['id'].tolist()
    data_dict = {}
    for item in key:
        data_dict[item] = (head_d.loc[head_d['id'] == item]['rank'].tolist()[0],
                           head_d.loc[head_d['id'] == item]['rankUpDown'].tolist()[0],
                           head_d.loc[head_d['id'] == item]['title'].tolist()[0],
                           head_d.loc[head_d['id'] == item]['fullTitle'].tolist()[0],
                           head_d.loc[head_d['id'] == item]['year'].tolist()[0],
                           head_d.loc[head_d['id'] == item]['crew'].tolist()[0],
                           head_d.loc[head_d['id'] == item]['imDbRating'].tolist()[0],
                           head_d.loc[head_d['id'] == item]['imDbRatingCount'].tolist()[0])

    for key in data_dict.keys():
        cursor.execute("""INSERT INTO pop_shows (id, rank, rankUpDown, title, fulLTitle, crew, year, imDbRating,
        imDbRatingCount) VALUES (?,?,?,?,?,?,?,?,?)""", (key, data_dict[key][0], data_dict[key][1],
                                                         data_dict[key][2], data_dict[key][3],
                                                         data_dict[key][4], data_dict[key][5],
                                                         data_dict[key][6], data_dict[key][7]))
        conn.commit()


def populate_rankUpDown(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""INSERT INTO movie_upDownTrend
                   SELECT id, title, rankUpDown
                   FROM pop_movies
                   ORDER BY rankUpDown DESC
                   LIMIT 3""")

    cursor.execute("""INSERT INTO movie_upDownTrend
                       SELECT id, title, rankUpDown
                       FROM pop_movies
                       ORDER BY rankUpDown ASC
                       LIMIT 1""")
    conn.commit()


def populate_pop_movies(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    pop_movies = get_data03()
    kii = pop_movies['id'].tolist()
    data_dict02 = {}
    for item in kii:
        data_dict02[item] = (pop_movies.loc[pop_movies['id'] == item]['rank'].tolist()[0],
                             pop_movies.loc[pop_movies['id'] == item]['rankUpDown'].tolist()[0],
                             pop_movies.loc[pop_movies['id'] == item]['title'].tolist()[0],
                             pop_movies.loc[pop_movies['id'] == item]['fullTitle'].tolist()[0],
                             pop_movies.loc[pop_movies['id'] == item]['year'].tolist()[0],
                             pop_movies.loc[pop_movies['id'] == item]['crew'].tolist()[0],
                             pop_movies.loc[pop_movies['id'] == item]['imDbRating'].tolist()[0],
                             pop_movies.loc[pop_movies['id'] == item]['imDbRatingCount'].tolist()[0])

    for key in data_dict02.keys():
        cursor.execute("""INSERT INTO pop_movies (id, rank, rankUpDown, title, fulLTitle, crew, year, imDbRating,
        imDbRatingCount) VALUES (?,?,?,?,?,?,?,?,?)""", (key, data_dict02[key][0], data_dict02[key][1],
                                                         data_dict02[key][2], data_dict02[key][3],
                                                         data_dict02[key][4], data_dict02[key][5],
                                                         data_dict02[key][6], data_dict02[key][7]))
        conn.commit()


def populate_movie250(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    movie250 = get_movies()
    keys = movie250['id'].tolist()
    data_dicts = {}
    for item in keys:
        data_dicts[item] = (movie250.loc[movie250['id'] == item]['title'].tolist()[0],
                            movie250.loc[movie250['id'] == item]['fullTitle'].tolist()[0],
                            movie250.loc[movie250['id'] == item]['crew'].tolist()[0],
                            movie250.loc[movie250['id'] == item]['year'].tolist()[0],
                            movie250.loc[movie250['id'] == item]['imDbRating'].tolist()[0],
                            movie250.loc[movie250['id'] == item]['imDbRatingCount'].tolist()[0])

    for key in data_dicts.keys():
        cursor.execute("""INSERT INTO movie_headlines (id, title, full_title, crew, year, rating, rating_count)
                                  VALUES (?,?,?,?,?,?,?)""", (key, data_dicts[key][0], data_dicts[key][1],
                                                              data_dicts[key][2], data_dicts[key][3],
                                                              data_dicts[key][4],
                                                              data_dicts[key][5]))
        conn.commit()


def janitorial(cursor: sqlite3.Cursor):
    try:
        cursor.execute("""
                       DROP TABLE IF EXISTS pop_shows;
                       """)

        cursor.execute("""
                       DROP TABLE IF EXISTS pop_movies;
                       """)

        cursor.execute("""
                       DROP TABLE IF EXISTS movie_upDownTrend;
                       """)

        cursor.execute("""
                       DROP TABLE IF EXISTS headline_data;
                       """)

        cursor.execute("""
                       DROP TABLE IF EXISTS movie_headlines;
                       """)

        cursor.execute("""
                       DROP TABLE IF EXISTS ratings_data;
                       """)

    except sqlite3.Error:
        print("Un-cleanable Mess")
    finally:
        print("Done")


def main():
    pop_csv()
    name = 'movie_api.db'
    conn, cursor = open_db(name)
    janitorial(cursor)
    conn.commit()
    database_stuff.main()
    db_setter(cursor)
    populate_movie250(cursor, conn)
    populate_pop_movies(cursor, conn)
    populate_pop_shows(cursor, conn)
    populate_rankUpDown(cursor, conn)
    conn.commit()
    close_db(conn)


main()
