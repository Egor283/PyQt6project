from PyQt6.QtWidgets import QWidget
from root_design import Root_design
from Project.coefficient import Coefficient
from description_root_function import Description_root_function


class Root(QWidget, Root_design):
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
                self.descripion_line = Description_root_function(self.coefficient)
                self.descripion_line.show()
                self.close()
            except ValueError:
                self.cof = Coefficient('Вы написали не числа')
                self.cof.show()