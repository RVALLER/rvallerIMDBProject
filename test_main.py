import requests
from typing import Tuple

import secret
import sqlite3


def extract():
    # ------------------------------ Part I Start ------------------------------- #
    url = f"https://imdb-api.com/en/API/Top250TVs/{secret.main()}"
    results = requests.get(url)

    if results.status_code != 200:
        print("Uh-Oh")
        return
    data_pull = results.json()
    thelist = data_pull['items']  # Takes only the pertinent info from the data scrape and appends to dictionary
    return thelist

#
# def setup_db(cursor: sqlite3.Cursor):
#     cursor.execute('''CREATE TABLE IF NOT EXISTS tv_data(id TEXT PRIMARY KEY,
#             title TEXT NOT NULL,
#             full_title TEXT NOT NULL,
#             crew TEXT,
#             year INTEGER NOT NULL,
#             rating FLOAT DEFAULT 0,
#             rating_count FLOAT DEFAULT 0);''')
#
#
# test_dict = ['tt373892','Test Data On Ice','Test Data on Ice (2022)',
#                  'One man Wrecking Crew', '2022',
#                  '1','9001']
#
# def populate_tv_data(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
#
#     cursor.execute('''INSERT INTO tv_data (id,title,full_title,crew,year,rating,rating_count) VALUES(?,?,?,?,?,?,?)''',
#                    test_dict)
#
#     conn.commit()
#
#
# def check_func(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
#     cursor.execute('''SELECT * FROM tv_data''')
#     q = cursor.fetchall()
#     return q
#
#
# def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
#     db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
#     cursor = db_connection.cursor()  # get ready to read/write data
#     return db_connection, cursor
#
#
# def close_db(connection: sqlite3.Connection):
#     connection.commit()  # make sure any changes get saved
#     connection.close()

#
# def main():
#         name = 'dummy.db'
#         conn, cursor = open_db(name)
#         setup_db(cursor)
#         populate_tv_data(cursor,conn)
#         conn.commit()
#         close_db(conn)


#main()