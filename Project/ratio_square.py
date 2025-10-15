import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QWidget
from ratio_square_design import Square_design


class SecondForm(QWidget, Square_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)