import sys
from PyQt6 import uic
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from description_line_function_design import Description_line_design


class Description_line_function(QWidget, Description_line_design):
    def __init__(self, args):
        super().__init__()
        if args[0] == '1':
            self.k_label = ''
            self.k = '1'
        elif args[0] == '-1':
            self.k_label = '-'
            self.k = '-1'
        else:
            self.k_label = args[0]
            self.k = self.k_label
        self.b = args[1]
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        if float(self.k) and float(self.b):
            self.label.setText(f'y = {self.k_label}x + {self.b} ; линейная функция, графиком является прямая')
        elif float(self.k):
            if self.k == '1':
                self.label.setText(f'y = x ; линейная функция, графиком является прямая')
            elif self.k == '-1':
                self.label.setText(f'y = -x ; линейная функция, графиком является прямая')
            else:
                self.label.setText(f'y = {self.k_label}x ; линейная функция, графиком является прямая')
        elif float(self.b):
            self.label.setText(f'y = {self.b} ; линейная функция, графиком является прямая')
        if float(self.k) > 0:
            self.label_2.setText(f'f(x) возрастает')
        elif float(self.k) < 0:
            self.label_2.setText(f'f(x) убывает')
        else:
            self.label_2.setText(f'f(x) параллельно оси Ox')
        self.label_3.setText(f'Пересечение с осью y (0;{self.b})')
        fig, ax = plt.subplots()
        k, b = float(self.k), float(self.b)
        ax.set_ylim(-20, 20)
        ax.set_xlim(-20, 20)
        fig.set_size_inches(5, 4)
        ax.grid()
        x = np.linspace(-20, 20, 100)
        y = k * x + b
        plt.xlabel(' Ось x', fontsize=14)
        plt.ylabel('Ось y', fontsize=14)
        plt.title('График', fontsize=14)
        ax.plot(x, y)