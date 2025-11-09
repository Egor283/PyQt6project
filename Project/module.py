from PyQt6.QtWidgets import QWidget
from module_design import Module_design
from description_module_function import Description_module_function
from Project.coefficient import Coefficient


class Module(QWidget, Module_design):
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
                self.descripion_module = Description_module_function(self.coefficient)
                self.descripion_module.show()
                self.close()
            except ValueError:
                self.cof = Coefficient('Вы написали не числа')
                self.cof.show()