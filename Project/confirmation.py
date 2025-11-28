from PyQt6.QtWidgets import QWidget
from confirmation_design import Confirmation_design


class Confirmation(QWidget, Confirmation_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.intiUi()

    def intiUi(self):
        self.pushButton.clicked.connect(self.doo)

    def doo(self):
        self.close()