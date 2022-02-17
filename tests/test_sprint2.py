from typing import Tuple
import requests
import secrets
import sqlite3


# basic test to make sure I had tests working
def test_add():
    assert 2 + 2 == 4


# This is a function to pull the list needed for  correct retrieval method
def data_scrape():
    url = f"https://imdb-api.com/en/API/Top250TVs/{secrets.API_KEY}"
    results = requests.get(url)
    data_pull = results.json()
    the_list = data_pull['items']  # Takes only the pertinent info from the data scrape and appends to dictionary
    return the_list


# This test made sure my method for scraping top 250 worked by applying a spliced version of the original.
def test_correct_retrieval():
    url = f"https://imdb-api.com/en/API/Top250TVs/{secrets.API_KEY}"
    results = requests.get(url)
    data_pull = results.json()
    the_list = data_pull['items']
    item = len(the_list)
    print(item)
    assert item == 250


# Bear with me, I know its grotesque, but this method tests out my datbase creation methods by feeding some dummy
# data to a dummy database. I know, I shouldn't call them names. Comes with all of dbstuff.py's bells and whistles
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

    def test_correct_new_table(curs: sqlite3.Cursor):
        curs.execute('''CREATE TABLE IF NOT EXISTS dummy_pop(
                    id TEXT PRIMARY KEY,
                    rank TEXT,
                    rankUpDown FLOAT,
                    title TEXT,
                    fullTitle INTEGER,
                    year FLOAT DEFAULT 0,
                    crew TEXT,
                    imDbRating TEXT,
                    imDbRatingCount FLOAT DEFAULT 0);''')

        curs.execute('''CREATE TABLE IF NOT EXISTS rankUpDown_dummy(
                    id TEXT PRIMARY KEY,
                    title TEXT,
                    rankUpDown FLOAT);''')

        test_dict_a = ['tt3723822', "Test Data on", "+100"]
        test_dict_b = ['tt3793822', "Test Data on 2", "-1000"]
        test_dict_c = ['tt3733822', "Test Data on 3", "+10"]
        test_dict_d = ['tt3713822', "Test Data From Hell", "+1000"]

        curs.execute('''INSERT INTO rankUpDown_dummy(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_a)
        curs.execute('''INSERT INTO rankUpDown_dummy(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_b)
        curs.execute('''INSERT INTO rankUpDown_dummy(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_c)
        curs.execute('''INSERT INTO rankUpDown_dummy(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_d)

        name = 'dummy.db'
        conn, cursor = open_db(name)
        setup_db(cursor)
        populate_tv_data(cursor, conn)
        conn.commit()
        cursor.execute('''SELECT id FROM tv_data''')
        res = cursor.fetchall()
        assert len(res) == 1
        # test_correct_new_table(cursor)
        # cursor.execute('''SELECT id from rankUpDown_dummy''')
        # tst = cursor.fetchall()
        # assert len(tst) == 4
        cursor.execute(''' SELECT title FROM tv_data''')
        results = cursor.fetchall()
        test_record = results[0]
        assert test_record[0] == 'Test Data On Ice'
        close_db(conn)
