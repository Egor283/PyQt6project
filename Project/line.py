import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from line_design import Line_design
from description_line_function import Description_line_function



class Line(QWidget, Line_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.doo)

    def doo(self):
        self.coefficient = [self.lineEdit.text(), self.lineEdit_2.text()]
        self.descripion_line = Description_line_function(self.coefficient)
        self.close()
        self.descripion_line.show()

    def _close_(self):
        self.close()