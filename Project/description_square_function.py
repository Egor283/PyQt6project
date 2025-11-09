import sys
from PyQt6 import uic
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QWidget
from description_fraction_function_design import Description_fraction_function_design


class Description_fraction_function(QWidget, Description_fraction_function_design):
    def __init__(self, args):
        super().__init__()
        self.move(515, 540)
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
        self.pushButton.clicked.connect(self.doo)
        if float(self.k) and float(self.b):
            self.label.setText(f'y = {self.k_label}/x + {self.b} ; дробная функция, графиком является гипербола')
        elif float(self.k) and not float(self.b):
            if self.k == '1':
                self.label.setText(f'y = 1/x ; дробная функция, графиком является гипербола')
            elif self.k == '-1':
                self.label.setText(f'y = -1/x ; дробная функция, графиком является гипербола')
            else:
                self.label.setText(f'y = {self.k_label}/x ; дробная функция, графиком является гипербола')
        else:
            self.label.setText(f'y = {self.b} ; дробная функция, графиком является гипербола')
        self.label_2.setText(f'D(f) x = (-∞;0)∩(0;+∞);E(f) y = (-∞;{self.b})∩({self.b};+∞)')
        if float(self.k) < 0:
            self.label_3.setText(f'f(x) ↗ возрастает')
        elif float(self.k) > 0:
            self.label_3.setText(f'f(x) ↘ убывает')
        else:
            self.label_3.setText(f'f(x) параллельно оси Ox')
        self.label_4.setText(f'Пересечение с Осью y на данном графике не существует')
        if float(self.b):
            self.x_0 = round(float(self.k) / -float(self.b), 2)
            self.label_5.setText(f'Нули функции y = 0 при x = {self.x_0}, ({self.x_0};0)')
        else:
            self.label_5.setText(f'Нулей не существует')
        x = np.linspace(-20, 20, 1000)
        fig, ax = plt.subplots()
        k, b = float(self.k), float(self.b)
        fig.set_size_inches(2, 2)
        ax.set_ylim(-20, 20)
        ax.set_xlim(-20, 20)
        fig.set_size_inches(5, 4)
        ax.grid()
        y = k / x + b
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.axhline(b)
        plt.xlabel('Ось x', fontsize=14)
        plt.ylabel('Ось y', fontsize=14)
        plt.title('График и асимптоты', fontsize=14)
        fig.canvas.manager.window.move(515, 75)
        ax.plot(x, y)
        plt.show()

    def doo(self):
        plt.close()
        self.close()