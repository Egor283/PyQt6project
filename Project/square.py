import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from square_design import Square_design


class Square(QWidget, Square_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)