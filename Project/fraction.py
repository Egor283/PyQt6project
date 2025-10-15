import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from fraction_design import Fraction_design


class Fraction(QWidget, Fraction_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)