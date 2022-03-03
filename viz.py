from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QTableWidgetItem
from Sprint_3 import open_db


class viz_data(QWidget):

    def go_viz_data(self):
        self.new_wind = viz_data()
        self.new_wind.show()

    def __init__(self):
        super(viz_data, self).__init__()
        self.tableWidget = None
        self.new_wind = None
        # self.setup_window()
        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(60, 800)