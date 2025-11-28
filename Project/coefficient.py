from PyQt6.QtWidgets import QWidget
from coefficient_design import Coefficient_design


class Coefficient(QWidget, Coefficient_design):
    def __init__(self, args):
        super().__init__()
        self.setupUi(self)
        self.label.setText(args)
        self.intiUi()

    def intiUi(self):
        self.pushButton.clicked.connect(self.doo)

    def doo(self):
        self.close()