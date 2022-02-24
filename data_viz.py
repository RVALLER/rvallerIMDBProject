# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_vizMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class vizmain(object):
    def __init__(self):
        self.pushButton_6 = None
        self.pushButton_5 = None
        self.pushButton_4 = None
        self.label_2 = None
        self.pushButton_3 = None
        self.pushButton_2 = None
        self.welcome = None
        self.label = None
        self.pushButton = None
        self.data_viz = None

    def setupViz(self, dialog):
        dialog.setObjectName("dviz")
        dialog.resize(1155, 810)
        dialog.setStyleSheet("")
        self.data_viz = QtWidgets.QWidget(dialog)
        self.data_viz.setGeometry(QtCore.QRect(-50, 10, 1200, 800))
        self.data_viz.setStyleSheet("QWidget#data_viz{\n"
                                    "font: 16pt \"MS Shell Dlg 2\";\n"
                                    "background-color:qlineargradient(spread:pad, x1:0, y1:0.00545455, x2:1, y2:1,"
                                    "stop:0 rgba(145, 135, 165, 255),"
                                    "stop:1 rgba(255, 255, 255, 255))}")
        self.data_viz.setObjectName("data_viz")
        self.welcome = QtWidgets.QLabel(self.data_viz)
        self.welcome.setGeometry(QtCore.QRect(400, 30, 551, 51))
        self.welcome.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";color: White;")
        self.welcome.setObjectName("welcome")
        self.label = QtWidgets.QLabel(self.data_viz)
        self.label.setGeometry(QtCore.QRect(430, 90, 351, 41))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";color: white;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.data_viz)
        self.pushButton.setGeometry(QtCore.QRect(480, 150, 251, 51))
        self.pushButton.setStyleSheet("border-radius:20px;\n"
                                      "background-color: rgb(219, 212, 255);\n"
                                      "font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.data_viz)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 230, 251, 51))
        self.pushButton_2.setStyleSheet("border-radius:20px;\n"
                                        "background-color:rgb(219, 212, 255);\n"
                                        "font:12pt\"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.data_viz)
        self.label_2.setGeometry(QtCore.QRect(510, 310, 201, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";color: white;")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.data_viz)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 360, 251, 51))
        self.pushButton_3.setStyleSheet("border-radius:20px;\n"
                                        "background-color: rgb(219, 212, 255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.data_viz)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 420, 251, 51))
        self.pushButton_4.setStyleSheet("border-radius:20px;\n"
                                        "background-color: rgb(219, 212, 255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.data_viz)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 480, 251, 51))
        self.pushButton_5.setStyleSheet("border-radius:20px;\n"
                                        "background-color: rgb(219, 212, 255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.data_viz)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 540, 251, 51))
        self.pushButton_6.setStyleSheet("border-radius:20px;\n"
                                        "background-color: rgb(219, 212, 255);\n"
                                        "font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.welcome.setText(_translate("dialog", "IMD-Data: Data Viz"))
        self.label.setText(_translate("dialog", "Please Select One of the Following:"))
        self.pushButton.setText(_translate("dialog", "Movies Top 250 & Pop Overlap"))
        self.pushButton_2.setText(_translate("dialog", "TV Top 250 Pop Overlap"))
        self.label_2.setText(_translate("dialog", "For Graph Displays:"))
        self.pushButton_3.setText(_translate("dialog", "Pop Movie UpTrend"))
        self.pushButton_4.setText(_translate("dialog", "Pop Movie DownTrend"))
        self.pushButton_5.setText(_translate("dialog", "Pop TV UpTrend"))
        self.pushButton_6.setText(_translate("dialog", "Movies Top 250 & Pop Overlap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = vizmain()
    ui.setupViz(dialog)
    dialog.show()
    sys.exit(app.exec_())

