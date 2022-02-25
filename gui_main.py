import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow, QPushButton, QLabel, QMessageBox, \
    QStackedWidget
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtSql
import functools
import sqlite3
from Sprint_3 import pop_all, empty_all


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



# main
app = QApplication(sys.argv)
mains = mainwin()
widget = QStackedWidget()
widget.addWidget(mains)
widget.setFixedHeight(800)
widget.setFixedWidth(990)
widget.show()
app.exec_()
