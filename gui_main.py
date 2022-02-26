import sqlite3
import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QStackedWidget
from PyQt5.uic import loadUi
from Sprint_3 import pop_all, empty_all, open_db, close_db


class mainwin(QDialog):
    def __init__(self):
        super(mainwin, self).__init__()
        loadUi("main_win.ui", self)
        self.viz_main.clicked.connect(self.gotoviz)
        self.upD.clicked.connect(self.update_data)

    def gotoviz(self):
        vizmain = vizdata()
        widget.addWidget(vizmain)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def update_data(self):
        message = QMessageBox(self)
        message.setText("Database Updated. For More fun, Select 'Visualize Data' ")
        message.setWindowTitle("Data Manager")
        message.show()
        empty_all()
        pop_all()


class Mov_overlap(QDialog):
    def __init__(self):
        super(Mov_overlap, self).__init__()

        self.topop_mov.clicked.connect(self.goto_movOverlap)
        loadUi("top_movOverlap.ui", self)
        name = 'movie_api.db'
        conn, cursor = open_db(name)
        cursor.execute('''SELECT
        fullTitle,rating,rating_count,rankUpDown FROM
        movie_headlines h
        INNER JOIN pop_movies p
        ON h.id = p.id''')
        self.mov_overlaps.setRowCount(0)

    def goto_movOverlap(self):
        m_over = Mov_overlap()
        widget.addWidget(m_over)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class vizdata(QDialog):
    def __init__(self):
        super(vizdata, self).__init__()
        loadUi("data_vizMain.ui", self)


# main
app = QApplication(sys.argv)
mains = mainwin()
widget = QStackedWidget()
widget.addWidget(mains)
widget.setFixedHeight(811)
widget.setFixedWidth(1261)
widget.show()
app.exec_()
