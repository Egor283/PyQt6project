import sys
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QWidget
from confirmation_design import Confirmation


class Confirmation(QWidget, Confirmation):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.intiUi()

    def intiUi(self):
        self.pushButton.clicked.connect(self.doo)

    def doo(self):
        self.close()