from PyQt6.QtWidgets import QWidget
from line_design import Line_design
from description_line_function import Description_line_function
from Project.coefficient import Coefficient



class Line(QWidget, Line_design):
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
                self.coefficient = [self.lineEdit.text(), self.lineEdit_2.text()]
                self.descripion_line = Description_line_function(self.coefficient)
                self.descripion_line.show()
                self.close()
            except ValueError:
                self.cof = Coefficient('Вы написали не числа')
                self.cof.show()