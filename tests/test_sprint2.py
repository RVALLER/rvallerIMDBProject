from typing import Tuple
import requests
import secrets
import sqlite3


def data_scrape():
    url = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(url)
    data_pull = results.json()
    the_list = data_pull['items']  # Takes only the pertinent info from the data scrape and appends to dictionary
    return the_list


def test_correct_retrieval():
    assert len(data_scrape()) == 250


def test_dbStuff():
    def setup_db(curs: sqlite3.Cursor):
        curs.execute('''CREATE TABLE IF NOT EXISTS tv_data(id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                full_title TEXT NOT NULL,
                crew TEXT,
                year INTEGER NOT NULL,
                rating FLOAT DEFAULT 0,
                rating_count FLOAT DEFAULT 0);''')

    test_dict = ['tt373892', 'Test Data On Ice', 'Test Data on Ice (2022)',
                 'One man Wrecking Crew', '2022',
                 '1', '9001']

    def populate_tv_data(crss: sqlite3.Cursor, cn: sqlite3.Connection):
        crss.execute(
            '''INSERT INTO tv_data (id,title,full_title,crew,year,rating,rating_count) VALUES(?,?,?,?,?,?,?)''',
            test_dict, )
        cn.commit()

    def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
        curs = db_connection.cursor()  # get ready to read/write data
        return db_connection, curs

    def close_db(connection: sqlite3.Connection):
        connection.commit()  # make sure any changes get saved
        connection.close()

    name = 'dummy.db'
    conn, cursor = open_db(name)
    setup_db(cursor)
    populate_tv_data(cursor, conn)
    conn.commit()
    cursor.execute('''SELECT id FROM tv_data''')
    res = cursor.fetchall()
    assert len(res) == 1
    cursor.execute(''' SELECT title FROM tv_data''')
    results = cursor.fetchall()
    test_record = results[0]
    assert test_record[0] == 'Test Data On Ice'
    close_db(conn)
