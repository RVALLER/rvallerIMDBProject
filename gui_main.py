import sys
from Sprint_3 import pop_all, empty_all, open_db, close_db
import PySide6
from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem, QMessageBox


class main_menu(QWidget):
    def __init__(self):
        super().__init__()
        self.new_wind = None
        self.go_visualize_d()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("IMD-Data Main Menu")
        # display_list = QListWidget(self)
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
        self.show()

    def update_data(self):
        message = QMessageBox(self)
        message.setText("Database Updated. For More fun, Select 'Visualize Data' ")
        message.setWindowTitle("Data Manager")
        message.show()
        empty_all()
        pop_all()

    def go_visualize_d(self):
        self.new_wind = viz_data()
        self.new_wind.show()


class viz_data(QWidget):
    def __init__(self):
        super(viz_data, self).__init__()
        self.list_control = None
        self.setup_window()
        self.data = self.get_data()

    def setup_window(self):
        self.setWindowTitle("IMD-Data Data Visualization")
        # display_list = QListWidget(self)
        self.setGeometry(300, 100, 1080, 900)
        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(900, 850)

        pop_mov_o = QPushButton("Movies Overlap", self)
        pop_mov_o.clicked.connect(self.show_list)
        pop_mov_o.resize(pop_mov_o.sizeHint())
        pop_mov_o.move(900, 800)

    def show_list(self):
        display_list = QListWidget(self)
        self.list_control = display_list
        self.data_to_list(self.data)
        display_list.resize(400, 350)
        self.setGeometry(300, 100, 400, 500)

        self.show()

    def data_to_list(self, data: list[dict]):
        for key in data:
            display_text = f"{key['full_title']}\t\t{key['rating']}\t\t{key['rating_count']}\t\t{key['rankUpDown']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)

    def get_data(self):
        name = "movie_api.db"
        conn, curs = open_db(name)
        curs.execute(f"""SELECT t.full_title, t.rating, t.rating_count, p.rankUpDown
                                     FROM movie_headlines t
                                     INNER JOIN pop_movies p 
                                     ON t.id = p.id""")
        overlap = curs.fetchall()
        new_overlap = to_dict(overlap)
        return new_overlap


def to_dict(lst_tuples):
    var = [{i[0]: list(i[1:])} for i in lst_tuples]
    return var


def display_main():
    qt_app = PySide6.QtWidgets.QApplication(sys.argv)  # sys.argv is the list of command line arguments
    my_window = main_menu()
    my_window.show()
    sys.exit(qt_app.exec())


def main():
    display_main()


if __name__ == '__main__':
    main()
