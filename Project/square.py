from PyQt6.QtWidgets import QWidget
from square_design import Square_design
from coefficient import Coefficient
from description_square_function import Description_square_function


class Square(QWidget, Square_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.doo)
        self.pushButton_2.clicked.connect(self.doo_2)

    def doo(self):
        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '':
            self.cof = Coefficient('Вы не написали коэффициенты')
            self.cof.show()
        else:
            try:
                test = [float(self.lineEdit.text()), float(self.lineEdit_2.text()), float(self.lineEdit_3.text())]
                self.coefficient = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()]
                self.descripion_square = Description_square_function(self.coefficient)
                self.descripion_square.show()
            except ValueError:
                self.cof = Coefficient('Вы написали не числа')
                self.cof.show()

    def doo_2(self):
        self.close()