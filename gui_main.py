import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow, QPushButton, QLabel, QMessageBox, \
    QStackedWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtSql
import functools


def goviz():
    viz_main = vizdata()
    widget.setCurrentWidget(widget.setCurrentIndex(1))
    viz_main.show()


class mainwin(QDialog):
    def __init__(self):
        super(mainwin, self).__init__()
        loadUi("main_win.ui", self)
        self.viz_main.clicked.connect(self.gotoviz)

    def gotoviz(self):
        vizmain = vizdata()
        widget.addWidget(vizmain)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class vizdata(QDialog):
    def __init__(self):
        super(vizdata, self).__init__()
        loadUi("data_vizMain.ui", self)


class update_data(QDialog):
    def __init__(self):
        super(update_data, self).__init__()


# main
app = QApplication(sys.argv)
mains = mainwin()
widget = QStackedWidget()
widget.addWidget(mains)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
app.exec_()
