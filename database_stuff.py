import sqlite3
from typing import Tuple
import pandas as pd

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


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def main():
    conn, cursor = open_db("movie_api.db")
    setup_db(cursor)
    close_db(conn)



main()
