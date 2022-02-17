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

    test_dict_a = ['tt3723822', "Test Data on", 100]
    test_dict_b = ['tt3793822', "Test Data on 2", -1000]
    test_dict_c = ['tt3733822', "Test Data on 3", 10]
    test_dict_d = ['tt3713822', "Test Data From Hell", 1000]
    test_dict_e = ['tt3401320', "Back to the Data Again", -10]

    cursor.execute('''INSERT INTO dummy_pop(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_a)
    cursor.execute('''INSERT INTO dummy_pop(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_b)
    cursor.execute('''INSERT INTO dummy_pop(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_c)
    cursor.execute('''INSERT INTO dummy_pop(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_d)
    cursor.execute('''INSERT INTO dummy_pop(id,title,rankUpDown) VALUES(?,?,?)''', test_dict_e)


def populate_rankUpDownDummy(cursor: sqlite3.Cursor, conn: sqlite3.Connection):
    cursor.execute("""INSERT INTO rankUpDown_Dummy
                   SELECT id, title, rankUpDown
                   FROM dummy_pop
                   ORDER BY rankUpDown DESC
                   LIMIT 3""")
    conn.commit()

    cursor.execute("""INSERT INTO rankUpDown_Dummy
                       SELECT id, title, rankUpDown
                       FROM dummy_pop
                       ORDER BY rankUpDown ASC
                       LIMIT 1""")
    conn.commit()


def test_check_newTable():
    conn, curs = open_db("dummy.db")
    new_table(curs)
    curs.execute('''SELECT tbl_name FROM sqlite_master WHERE type='table'
                 AND tbl_name = 'rankUpDown_dummy'   ; ''')
    x = curs.fetchone()
    assert len(x) != 0


def test_check_write():
    conn, curs = open_db("dummy.db")
    new_table(curs)
    curs.execute('''SELECT id from dummy_pop''')
    contain_fetch = curs.fetchall()
    assert len(contain_fetch) == 5


def test_upDownChance():
    conn, curs = open_db("dummy.db")
    new_table(curs)
    populate_rankUpDownDummy(curs, conn)
    curs.execute('''SELECT rankUpDown from rankUpDown_dummy WHERE id = 'tt3793822' ''')
    query_hold = str(curs.fetchone())
    query_hold = query_hold.replace("'", "")
    query_hold = query_hold.replace(",", "")
    assert query_hold == "(-1000.0)"
    curs.execute('''SELECT rankUpDown from rankUpDown_dummy''')
    fetcher = curs.fetchall()
    assert len(fetcher) == 4
