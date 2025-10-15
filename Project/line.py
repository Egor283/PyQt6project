import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from line_design import Line_design


class Line(QWidget, Line_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)