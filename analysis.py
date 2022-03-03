from PyQt6.uic.properties import QtCore
from PySide6 import QtWidgets

from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QTableWidgetItem

from Sprint_3 import open_db


class analyze_data(QWidget):
    def __init__(self):
        super(analyze_data, self).__init__()
        self.tableWidget = None
        self.new_wind = None
        self.setup_window()

    def go_analyze_d(self):
        self.new_wind = analyze_data()
        self.new_wind.show()

    def setup_window(self):
        self.setWindowTitle("IMD-Data Data Visualization")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.resize(655, 766)
        self.tableWidget.setObjectName("tableWidget")
        self.setGeometry(300, 100, 1150, 900)
        # self.tableWidget.setColumnCount(3)

        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(60, 800)

        pop_mov_o = QPushButton("Movies Overlap", self)
        pop_mov_o.clicked.connect(self.show_list_1)
        pop_mov_o.resize(pop_mov_o.sizeHint())
        pop_mov_o.move(900, 800)

        pop_tv_o = QPushButton("TV Overlap", self)
        pop_tv_o.clicked.connect(self.show_list_2)
        pop_tv_o.resize(pop_mov_o.sizeHint())
        pop_tv_o.move(1000, 800)

        pop_tv_rud = QPushButton("Sort Pop TV by Rank UpDown", self)
        pop_tv_rud.clicked.connect(self.sort_show_rud)
        pop_tv_rud.resize(pop_tv_rud.sizeHint())
        pop_tv_rud.move(916, 765)

        pop_tv_r = QPushButton("Sort Pop TV by Ratings", self)
        pop_tv_r.clicked.connect(self.sort_show_ratings)
        pop_tv_r.resize(pop_tv_r.sizeHint())
        pop_tv_r.move(933, 830)

        pop_mov_r = QPushButton("Sort Pop Movies by Ratings", self)
        pop_mov_r.clicked.connect(self.sort_mov_r)
        pop_mov_r.resize(pop_mov_r.sizeHint())
        pop_mov_r.move(925, 734)

        pop_mov_rud = QPushButton("Sort Pop Movies by RankUpDown", self)
        pop_mov_rud.clicked.connect(self.sort_mov_rud)
        pop_mov_rud.resize(pop_mov_rud.sizeHint())
        pop_mov_rud.move(909, 704)

        top_250 = QPushButton("Show Top 250 shows", self)
        top_250.clicked.connect(self.show_250)
        top_250.resize(top_250.sizeHint())
        top_250.move(680, 763)

    def show_list_1(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        query = f"""SELECT t.full_title, t.rating, p.rankUpDown
                        FROM movie_headlines t
                        INNER JOIN pop_movies p 
                        ON t.id = p.id"""
        curs.execute(query)
        result = curs.fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def show_250(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        query = f"""SELECT full_title, rating
                    FROM headline_data
                    """
        curs.execute(query)
        result = curs.fetchall()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def show_list_2(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        query = f"""SELECT t.full_title, t.rating, p.rankUpDown
                FROM headline_data t
                INNER JOIN pop_shows p 
                ON t.id = p.id"""
        curs.execute(query)
        result = curs.fetchall()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def sort_show_rud(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        query = f"""SELECT fullTitle, imDbRating, rankUpDown
                FROM pop_shows
                ORDER BY rankUpDown DESC"""
        curs.execute(query)
        result = curs.fetchall()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def sort_show_ratings(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        query = f"""SELECT fullTitle, imDbRating, rankUpDown
                FROM pop_shows
                ORDER BY imDbRating DESC"""
        curs.execute(query)
        result = curs.fetchall()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def sort_mov_rud(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        query = f"""SELECT fullTitle, imDbRating, rankUpDown
                        FROM pop_movies
                        ORDER BY rankUpDown DESC"""
        curs.execute(query)
        result = curs.fetchall()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def sort_mov_r(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        query = f"""SELECT fullTitle, imDbRating, rankUpDown
                        FROM pop_movies
                        ORDER BY imDbRating DESC"""
        curs.execute(query)
        result = curs.fetchall()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))