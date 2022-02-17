from typing import Tuple
import sqlite3


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    curs = db_connection.cursor()  # get ready to read/write data
    return db_connection, curs


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def new_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS dummy_pop(
                   id TEXT PRIMARY KEY,
                   rank TEXT,
                   rankUpDown FLOAT,
                   title TEXT,
                   fullTitle INTEGER,
                   year FLOAT DEFAULT 0,
                   crew TEXT,
                   imDbRating TEXT,
                   imDbRatingCount FLOAT DEFAULT 0);''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS rankUpDown_dummy(
                   id TEXT PRIMARY KEY,
                   title TEXT,
                   rankUpDown FLOAT);''')

    test_dict_a = ['tt3723822', "Test Data on", "+100"]
    test_dict_b = ['tt3793822', "Test Data on 2", "-1000"]
    test_dict_c = ['tt3733822', "Test Data on 3", "+10"]
    test_dict_d = ['tt3713822', "Test Data From Hell", "+1000"]

    cursor.execute('''INSERT INTO rankUpDown_dummy(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_a)
    cursor.execute('''INSERT INTO rankUpDown_dummy(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_b)
    cursor.execute('''INSERT INTO rankUpDown_dummy(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_c)
    cursor.execute('''INSERT INTO rankUpDown_dummy(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_d)


def test_newTable():
    curs, conn = open_db("dummy.db")


