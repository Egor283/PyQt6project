import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget
from description_fraction_function_design import Description_fraction_function_design


class Description_fraction_function(QWidget, Description_fraction_function_design):
    def __init__(self, args):
        super().__init__()
        self.move(515, 540)
        self.k_label = args[0]
        self.k = self.k_label
        self.b = args[1]
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.doo)
        k, b = float(self.k), float(self.b)
        if k and b:
            if b > 0:
                self.label.setText(f'y = {self.k_label}/x + {self.b}; дробная функция, графиком является гипербола')
            else:
                self.label.setText(f'y = {self.k_label}/x - {self.b[1:]}; дробная функция, графиком является гипербола')
            self.label_2.setText(f'D(f) x = (-∞;0)∩(0;+∞);E(f) y = (-∞;{self.b})∩({self.b};+∞)')
            if k < 0:
                self.label_3.setText(f'f(x) ↗ возрастает')
            elif k > 0:
                self.label_3.setText(f'f(x) ↘ убывает')
            else:
                self.label_3.setText(f'f(x) параллельно оси Ox')
            self.label_4.setText(f'Пересечение с осью y на данном графике не существует')
            if b:
                x_0 = round(k / -b, 3)
                self.label_5.setText(f'Нули функции y = 0 при x = {x_0}, ({x_0};0)')
            else:
                self.label_5.setText(f'Нулей не существует')
        elif k and not b:
            self.label.setText(f'y = {self.k_label}/x; дробная функция, графиком является гипербола')
            self.label_2.setText(f'D(f) x = (-∞;0)∩(0;+∞);E(f) y = (-∞;{self.b})∩({self.b};+∞)')
            if k < 0:
                self.label_3.setText(f'f(x) ↗ возрастает')
            elif k > 0:
                self.label_3.setText(f'f(x) ↘ убывает')
            else:
                self.label_3.setText(f'f(x) параллельно оси Ox')
            self.label_4.setText(f'Пересечение с осью y на данном графике не существует')
            self.label_5.setText(f'Нулей не существует')
        elif not k and not b:
            self.label.setText(f'y = 0; линейная функция, графиком является прямая')
            self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = 0')
            self.label_3.setText(f'f(x) параллельно оси Ox')
            self.label_4.setText(f'Пересечение с осью y (0;0)')
            self.label_5.setText(f'y = 0 при любом x')
        else:
            self.label.setText(f'y = {self.b}; линейная функция, графиком является прямая')
            self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = {self.b}')
            self.label_3.setText(f'f(x) параллельно оси Ox')
            self.label_4.setText(f'Пересечение с осью y (0;{self.b})')
            self.label_5.setText(f'Нулей не существует')
        x = np.linspace(-20, 20, 1000)
        fig, ax = plt.subplots()
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