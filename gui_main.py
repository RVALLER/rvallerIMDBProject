import sys
import analysis
from Sprint_3 import pop_all, empty_all
import PySide6
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox


class main_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.new_wind = None
        # self.go_visualize_d()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("IMD-Data Main Menu")
        self.setGeometry(300, 100, 1150, 900)
        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(900, 850)

        update_data_button = QPushButton("Update Data", self)
        update_data_button.clicked.connect(self.update_data)
        update_data_button.resize(update_data_button.sizeHint())
        update_data_button.move(900, 800)

        visualize_data = QPushButton("Visualize Data", self)
        visualize_data.clicked.connect(self.go_visualize_d)
        visualize_data.resize(visualize_data.sizeHint())
        visualize_data.move(1010, 800)

    def update_data(self):
        message = QMessageBox(self)
        message.setText("Database Updated. For More fun, Select 'Visualize Data' ")
        message.setWindowTitle("Data Manager")
        message.show()
        empty_all()
        pop_all()

    def go_visualize_d(self):
        self.new_wind = analysis.analyze_data()
        self.new_wind.show()
        self.close_window()

    def close_window(self):
        self.close()


def display_main():
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = main_menu()
    my_window.show()
    sys.exit(qt_app.exec())


def main():
    display_main()


if __name__ == '__main__':
    main()
