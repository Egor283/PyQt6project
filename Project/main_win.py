import sys
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QMessageBox
from Project.main_win_design import Ui_MainWindow
from confirmation import Confirmation
from line import Line
from square import Square
from module import Module
from root import Root
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
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.doo)

    def doo(self):
        for i in self.radio_button_group.buttons():
            if i.isChecked():
                self.radio_button = i.text()[-2]
        if self.radio_button == '1':
            dialog = QMessageBox().question(self, '', 'Вы уверены в своем  выборе',
                                            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if dialog == QMessageBox.StandardButton.Yes:
                self.line = Line()
                self.line.show()
        elif self.radio_button == '2':
            dialog = QMessageBox().question(self, '', 'Вы уверены в своем  выборе',
                                            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if dialog == QMessageBox.StandardButton.Yes:
                self.module = Module()
                self.module.show()
        elif self.radio_button == '3':
            dialog = QMessageBox().question(self, '', 'Вы уверены в своем  выборе',
                                            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if dialog == QMessageBox.StandardButton.Yes:
                self.root = Root()
                self.root.show()
        elif self.radio_button == '5':
            dialog = QMessageBox().question(self, '', 'Вы уверены в своем  выборе',
                                            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if dialog == QMessageBox.StandardButton.Yes:
                self.fraction = Fraction()
                self.fraction.show()
        elif self.radio_button == '6':
            dialog = QMessageBox().question(self, '', 'Вы уверены в своем  выборе',
                                            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if dialog == QMessageBox.StandardButton.Yes:
                self.square = Square()
                self.square.show()
        else:
            self.confirmation = Confirmation(self)
            self.confirmation.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Win()
    ex.show()
    sys.exit(app.exec())