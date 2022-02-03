import sqlite3
from typing import Tuple

def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS headline_data( 
        id TEXT PRIMARY KEY, 
        title TEXT NOT NULL,
        full_title TEXT NOT NULL,
        crew TEXT,
        rating FLOAT DEFAULT 0,
        rating_count FLOAT DEFAULT 0);''')

    # cursor.execute('''CREATE TABLE IF NOT EXISTS ratings_data(
	#     id TEXT NOT NULL,
	#     total_rating INTEGER NOT NULL,
	#     total_rating_votes INTEGER,
	#     10Rating%	INTEGER NOT NULL,
	#     10RatingVotes	INTEGER NOT NULL,
	#     9Rating% INTEGER NOT NULL,
	#     9RatingVotes INTEGER NOT NULL,
	#     8Rating%	INTEGER NOT NULL,
	#     8RatingVotes	INTEGER NOT NULL,
	#     7Rating%	INTEGER NOT NULL,
	#     7RatingVotes	INTEGER NOT NULL,
	#     6Rating%	INTEGER NOT NULL,
	#     6RatingVotes	INTEGER NOT NULL,
	#     5Rating%	INTEGER NOT NULL,
	#     4Rating%	INTEGER NOT NULL,
	#     4RatingVotes	INTEGER NOT NULL,
	#     3Rating%	INTEGER NOT NULL,
	#     3RatingVotes	INTEGER NOT NULL,
	#     2Rating%	INTEGER NOT NULL,
	#     2RatingVotes	INTEGER NOT NULL,
	#     1Rating%	INTEGER NOT NULL,
	#     1RatingVotes	INTEGER NOT NULL,
	#     FOREIGN KEY id REFERENCES headline_data id);''')


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def main():
    conn, cursor = open_db("movie_api.sqlite")
    setup_db(cursor)
    close_db(conn)


main()
