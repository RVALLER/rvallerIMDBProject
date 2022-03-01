import sqlite3
import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication, QStackedWidget, QTableWidgetItem, QTableView, \
    QListWidget, QListWidgetItem
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


class vizdata(QDialog):
    def __init__(self):
        super(vizdata, self).__init__()
        loadUi("data_vizMain.ui", self)
        self.back.clicked.connect(self.CancelButton)
        self.topop_mov.clicked.connect(self.goTopPopOv)

    def goTopPopOv(self):
        popMovOv = pop250MovOlap()
        widget.addWidget(popMovOv)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def CancelButton(self):
        newWind = mainwin()
        widget.addWidget(newWind)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class pop250MovOlap(QDialog):
    def __init__(self):
        super(pop250MovOlap, self).__init__()
        name = 'movie_api.db'
        open_db(name)
        loadUi("top_movOverlap.ui", self)
        self.back.clicked.connect(self.CancelButton)
        self.get_overlap()

    def CancelButton(self):
        newWind = vizdata()
        widget.addWidget(newWind)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def get_overlap(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        curs.execute(f"""SELECT t.full_title, t.rating, t.rating_count, p.rankUpDown
                             FROM movie_headlines t
                             INNER JOIN pop_movies p 
                             ON t.id = p.id""")
        records = curs.fetchall()
        to_dict(records)
        self.put_data_in_list(self.records)


def put_data_in_list(self, data):
    numrows = len(data)
    numcols = len(data[0])
    self.movo.setColumnCount(numcols)
    self.movo.setRowCount(numrows)
    for row in range(numrows):
        for column in range(numcols):
            self.movo.setItem(row, column, QTableWidgetItem((data[row][column])))


def to_dict(lst_tuples):
    result = [dict(el) for el in lst_tuples]
    return result


# main
app = QApplication(sys.argv)
mains = mainwin()
widget = QStackedWidget()
widget.addWidget(mains)
widget.setFixedHeight(811)
widget.setFixedWidth(1261)
widget.show()
app.exec_()
