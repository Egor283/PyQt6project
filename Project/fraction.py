from PyQt6.QtWidgets import QWidget
from fraction_design import Fraction_design
from Project.coefficient import Coefficient
from description_fraction_function import Description_fraction_function


class Fraction(QWidget, Fraction_design):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
            self.pushButton.clicked.connect(self.doo)

    def doo(self):
        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '':
            self.cof = Coefficient('Вы не написали коэффициенты')
            self.cof.show()
        else:
            try:
                test = [float(self.lineEdit.text()), float(self.lineEdit_2.text())]
                self.coefficient = [self.lineEdit.text(), self.lineEdit_2.text()]
                self.descripion_fraction = Description_fraction_function(self.coefficient)
                self.descripion_fraction.show()
                self.close()
            except ValueError:
                self.cof = Coefficient('Вы написали не числа')
                self.cof.show()