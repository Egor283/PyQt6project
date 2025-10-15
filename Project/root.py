import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from root_design import Root_design


class Root(QWidget, Root_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)