import io
import sys
from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QWidget
from main_win_design import Ui_MainWindow
from square import Square
from confirmation import Confirmation
from line import Line
from module import Module
from root import Root
from cubic import Cubic
from fraction import Fraction


class Main_Win(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.img = QImage('img_1.png')
        self.pixmap = QPixmap(self.img)
        self.image.setPixmap(self.pixmap)
        self.radio_button = '0'
        self.radio_button_group = QButtonGroup(self)
        self.radio_button_group.addButton(self.radioButton)
        self.radio_button_group.addButton(self.radioButton_2)
        self.radio_button_group.addButton(self.radioButton_3)
        self.radio_button_group.addButton(self.radioButton_4)
        self.radio_button_group.addButton(self.radioButton_5)
        self.radio_button_group.addButton(self.radioButton_6)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.doo)

    def doo(self):
        for i in self.radio_button_group.buttons():
            if i.isChecked():
                self.radio_button = i.text()[-2]
        if self.radio_button == '1':
            self.line = Line(self)
            self.line.show()
        elif self.radio_button == '2':
            self.module = Module(self)
            self.module.show()
        elif self.radio_button == '3':
            self.root = Root(self)
            self.root.show()
        elif self.radio_button == '4':
            self.cubic = Cubic(self)
            self.cubic.show()
        elif self.radio_button == '5':
            self.fraction = Fraction(self)
            self.fraction.show()
        elif self.radio_button == '6':
            self.second_form = Square(self)
            self.second_form.show()
        else:
            self.confirmation = Confirmation(self)
            self.confirmation.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Win()
    ex.show()
    sys.exit(app.exec())