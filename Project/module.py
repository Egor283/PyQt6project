import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from module_design import Module_design


class Module(QWidget, Module_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)