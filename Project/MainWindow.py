import io
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QWidget
from Project import *
from main_win_design import Ui_MainWindow
from ratio_square import SecondForm
from confirmation import Confirmation


class Main_Win(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.img = QImage('img_1.png')
        self.pixmap = QPixmap(self.img)
        self.image.setPixmap(self.pixmap)
        self.radio_button = '0'
        self.radio_button_group = QButtonGroup(self)
        self.radio_button_group.addButton(self.radioButton)
        self.radio_button_group.addButton(self.radioButton_2)
        self.radio_button_group.addButton(self.radioButton_3)
        self.radio_button_group.addButton(self.radioButton_4)
        self.radio_button_group.addButton(self.radioButton_5)
        self.radio_button_group.addButton(self.radioButton_6)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.doo)

    def doo(self):
        for i in self.radio_button_group.buttons():
            if i.isChecked():
                self.radio_button = i.text()[-2]
        if self.radio_button == '1':
            pass
        elif self.radio_button == '2':
            pass
        elif self.radio_button == '3':
            pass
        elif self.radio_button == '4':
            pass
        elif self.radio_button == '5':
            pass
        elif self.radio_button == '6':
            self.second_form = SecondForm(self, self.radio_button)
            self.second_form.show()
        else:
            self.confirmation = Confirmation(self)
            self.confirmation.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Win()
    ex.show()
    sys.exit(app.exec())