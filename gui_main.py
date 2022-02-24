import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow, QPushButton, QLabel, QMessageBox, \
    QStackedWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtSql
import functools


class mainwin(QDialog):
    def __init__(self):
        super(mainwin, self).__init__()
        loadUi("main_screen.ui", self)


class vizMain(QDialog):
    def __init__(self):
        super(vizMain, self).__init__()
        loadUi("data_vizMain.ui", self)



# main
app = QApplication(sys.argv)
mains = mainwin()
vizmain = vizMain()
widget = QStackedWidget()
widget.addWidget(mains)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
app.exec_()
