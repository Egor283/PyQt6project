import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from cubic_design import Cubic_design


class Cubic(QWidget, Cubic_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)