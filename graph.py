from PySide6.QtCore import QPointF
from PySide6.QtWidgets import QWidget
import pyqtgraph as pg
from Sprint_3 import open_db


def get_count(query):
    name = "movie_api.db"
    conn, curs = open_db(name)
    curs.execute(query)
    res_1 = curs.fetchall()
    count = 0
    for i in res_1:
        count += 1
    return count


class graph_stuff(QWidget):
    def __init__(self):
        super(graph_stuff, self).__init__()
        self.QScatterSeries = None
        self.graphWidget = None
        self.tableWidget = None
        self.new_wind = None
        self.setup_graph()

    def setup_graph(self):
        query_1 = f"""SELECT rankUpDown from pop_movies
                       WHERE rankUpDown > 0
                       ORDER by rankUpDown DESC"""

        query_2 = f"""SELECT rankUpDown from pop_movies
                           WHERE rankUpDown < 0
                           ORDER by rankUpDown DESC"""

        query_3 = f"""SELECT rankUpDown from pop_shows
                               WHERE rankUpDown > 0
                               ORDER by rankUpDown DESC"""

        query_4 = f"""SELECT rankUpDown from pop_shows
                                   WHERE rankUpDown < 0
                                   ORDER by rankUpDown DESC"""

        first = int(get_count(query_1))
        second = int(get_count(query_2))
        third = int(get_count(query_3))
        fourth = int(get_count(query_4))

        win = pg.plot()
        win.setBackground('w')
        title = "Up Down Trends"
        win.setWindowTitle(title)

        positions = [1, 2.25, 3, 4.25]
        heights = [first, second, third, fourth]

        bg = pg.BarGraphItem(x=positions, height=heights, width=0.333, brush='w')
        text = pg.TextItem('Movies Up', angle=90, color='green')
        text.setParentItem(bg)
        text.setX(positions[0])
        text.setAnchor(QPointF(0, .5))

        text2 = pg.TextItem('Movies Down', angle=90, color='red')
        text2.setParentItem(bg)
        text2.setX(positions[1])
        text2.setAnchor(QPointF(0, .5))

        text3 = pg.TextItem('Shows Up', angle=90, color='green')
        text3.setParentItem(bg)
        text3.setX(positions[2])
        text3.setAnchor(QPointF(0, 0.5))

        text4 = pg.TextItem('Shows Down', angle=90, color='red')
        text4.setParentItem(bg)
        text4.setX(positions[3])
        text4.setAnchor(QPointF(0, 0.5))

        styles = {'color': 'black', 'font-size': '20px'}
        win.setTitle("Trending Movies & Shows", **styles)
        win.setLabel('left', '# of Titles', **styles)
        win.setLabel('bottom', 'Type of Title | Trend', **styles)
        win.addItem(bg)

        win.show()
