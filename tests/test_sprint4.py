from Sprint_3 import open_db


def get_count(query):
    name = "dummy.db"
    conn, curs = open_db(name)
    curs.execute(query)
    res_1 = curs.fetchall()
    count = 0
    for i in res_1:
        count += 1
    return count


def test_data_counts():
    query_1 = """SELECT rankUpDown from dummy_pop
                           WHERE rankUpDown > 0
                           ORDER by rankUpDown DESC"""

    query_2 = """SELECT rankUpDown from dummy_pop
                               WHERE rankUpDown < 0
                               ORDER by rankUpDown DESC"""

    assert int(get_count(query_1)) == 3
    assert int(get_count(query_2)) == 2


def test_rankUpDown_sort():
    name = "dummy.db"
    conn, curs = open_db(name)
    query = """SELECT rankUpDown
                    FROM dummy_pop
                    ORDER BY rankUpDown DESC"""
    curs.execute(query)
    result = str(curs.fetchall())
    print(result)
    assert result == "[(1000.0,), (100.0,), (10.0,), (-10.0,), (-1000.0,)]"


def test_overlap():
    name = "dummy.db"
    conn, curs = open_db(name)
    query = """SELECT t.title
                    FROM dummy_top200 t
                    INNER JOIN dummy_pop p
                    ON t.id = p.id"""
    curs.execute(query)
    result = curs.fetchall()
    assert len(result) == 3
