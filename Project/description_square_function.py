import sys
from PyQt6 import uic
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QWidget
from description_square_function_design import Description_square_function_design


class Description_square_function(QWidget, Description_square_function_design):
    def __init__(self, args):
        super().__init__()
        self.move(515, 540)
        if args[0] == '1':
            self.a_label = ''
            self.a = '1'
        elif args[0] == '-1':
            self.a_label = '-'
            self.a = '-1'
        else:
            self.a_label = args[0]
            self.a = self.a_label
        if args[1] == '1':
            self.b_label = ''
            self.b = '1'
        elif args[1] == '-1':
            self.b_label = '-'
            self.b = '-1'
        else:
            self.b_label = args[1]
            self.b = self.b_label
        self.c = args[2]
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.doo)
        a, b, c = float(self.a), float(self.b), float(self.c)
        if a and b and c:
            if c > 0 and b > 0:
                self.label.setText(
                    f'y = {self.a_label}x2 + {self.b_label}x + {self.c}; квадратичная функция, графиком является парабола')
            elif c < 0 and b > 0:
                self.label.setText(
                    f'y = {self.a_label}x2 + {self.b_label}x - {self.c[1:]}; квадратичная функция, графиком является парабола')
            elif c > 0 and b < 0:
                self.label.setText(
                    f'y = {self.a_label}x2 - {self.b_label[1:]}x + {self.c}; квадратичная функция, графиком является парабола')
            else:
                self.label.setText(
                    f'y = {self.a_label}x2 - {self.b_label[1:]}x - {self.c[1:]}; квадратичная функция, графиком является парабола')
            x_0 = round(-b / (a * 2), 3)
            y_0 = round((x_0 ** 2 * a) + (b * x_0) + c, 3)
            self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = ({y_0};+∞)')
            if a > 0:
                self.label_3.setText(f'f(x) ↗ возрастает x ({x_0};+∞); f(x) ↘ убывает x (-∞;{x_0})')
            else:
                self.label_3.setText(f'f(x) ↗ возрастает x (-∞;{x_0}); f(x) ↘ убывает x ({x_0};+∞)')
            self.label_4.setText(f'Пересечение с Осью y (0;{self.c})')
            if (a > 0 and y_0 < 0) or (a < 0 and y_0 > 0):
                d = b ** 2 - 4 * a * c
                x_1, x_2 = -b + d ** 0.5 / (2 * a), -b - d ** 0.5 / (2 * a)
                self.label_5.setText(f'Нули функции y = 0 при x = {x_1} или {x_2}')
            elif (a > 0 and y_0 > 0) or (a < 0 and y_0 < 0):
                self.label_5.setText(f'Нулей функций нет')
            else:
                self.label_5.setText(f'Нули функции y = 0 при x = 0')
        elif not a and b and c:
            if b and c:
                self.label.setText(f'y = {self.b_label}x + {self.c} ; линейная функция, графиком является прямая')
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = (-∞;+∞)')
            elif b and not c:
                self.label.setText(f'y = {self.b_label}x ; линейная функция, графиком является прямая')
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = (-∞;+∞)')
            elif not b and c:
                self.label.setText(f'y = {self.c} ; линейная функция, графиком является прямая')
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = {self.c}')
            else:
                self.label.setText(f'y = 0 ; линейная функция, графиком является прямая')
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = 0')
            if b > 0:
                self.label_3.setText(f'f(x) ↗ возрастает')
            elif b < 0:
                self.label_3.setText(f'f(x) ↘ убывает')
            else:
                self.label_3.setText(f'f(x) параллельно оси Ox')
            self.label_4.setText(f'Пересечение с осью y (0;{self.c})')
            if b != 0:
                if b:
                    x_0 = round(-c / b, 2)
                else:
                    x_0 = 0
                self.label_5.setText(f'Нули функции y = 0 при x = {x_0}')
            elif b == 0 and c == 0:
                self.label_5.setText(f'y = 0 при любом x')
            else:
                self.label_5.setText(f'Нулей не существует')
        elif a and b and not c:
            self.label.setText(f'y = {self.a_label}x2 + {self.b_label}x; квадратичная функция, графиком является парабола')
            x_0 = round(-b / (a * 2), 3)
            y_0 = round((x_0 ** 2 * a) + (b * x_0) + c, 3)
            self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = ({y_0};+∞)')
            if a > 0:
                self.label_3.setText(f'f(x) ↗ возрастает x ({x_0};+∞); f(x) ↘ убывает x (-∞;{x_0})')
            else:
                self.label_3.setText(f'f(x) ↗ возрастает x (-∞;{x_0}); f(x) ↘ убывает x ({x_0};+∞)')
            self.label_4.setText(f'Пересечение с Осью y (0;{self.b})')
            self.label_5.setText(f'Нули функции y = 0 при x = 0')
        elif a and not b and c:
            self.label.setText(f'y = {self.a_label}x2 + {self.c}; квадратичная функция, графиком является парабола')
            x_0 = 0
            y_0 = round((x_0 ** 2 * a) + (b * x_0) + c, 3)
            self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = ({y_0};+∞)')
            if a > 0:
                self.label_3.setText(f'f(x) ↗ возрастает x ({x_0};+∞); f(x) ↘ убывает x (-∞;{x_0})')
            else:
                self.label_3.setText(f'f(x) ↗ возрастает x (-∞;{x_0}); f(x) ↘ убывает x ({x_0};+∞)')
            self.label_4.setText(f'Пересечение с Осью y (0;{self.b})')
            if (a > 0 and y_0 < 0) or (a < 0 and y_0 > 0):
                d = b ** 2 - 4 * a * c
                x_1, x_2 = -b + d ** 0.5 / (2 * a), -b - d ** 0.5 / (2 * a)
                self.label_5.setText(f'Нули функции y = 0 при x = {x_1} или {x_2}')
            elif (a > 0 and y_0 > 0) or (a < 0 and y_0 < 0):
                self.label_5.setText(f'Нулей функций нет')
            else:
                self.label_5.setText(f'Нули функции y = 0 при x = 0')
        elif a and not b and not c:
            self.label.setText(f'y = {self.a_label}x2; квадратичная функция, графиком является парабола')
            x_0 = 0
            y_0 = 0
            self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = ({y_0};+∞)')
            if a > 0:
                self.label_3.setText(f'f(x) ↗ возрастает x ({x_0};+∞); f(x) ↘ убывает x (-∞;{x_0})')
            else:
                self.label_3.setText(f'f(x) ↗ возрастает x (-∞;{x_0}); f(x) ↘ убывает x ({x_0};+∞)')
            self.label_4.setText(f'Пересечение с Осью y (0;{self.b})')
            self.label_5.setText(f'Нули функции y = 0 при x = 0')
        else:
            if b and c:
                self.label.setText(f'y = {self.b_label}x + {self.c} ; линейная функция, графиком является прямая')
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = (-∞;+∞)')
            elif b and not c:
                self.label.setText(f'y = {self.b_label}x ; линейная функция, графиком является прямая')
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = (-∞;+∞)')
            elif not b and c:
                self.label.setText(f'y = {self.c} ; линейная функция, графиком является прямая')
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = {self.c}')
            else:
                self.label.setText(f'y = 0 ; линейная функция, графиком является прямая')
                self.label_2.setText(f'D(f) x = (-∞;+∞);E(f) y = 0')
            if b > 0:
                self.label_3.setText(f'f(x) ↗ возрастает')
            elif b < 0:
                self.label_3.setText(f'f(x) ↘ убывает')
            else:
                self.label_3.setText(f'f(x) параллельно оси Ox')
            self.label_4.setText(f'Пересечение с осью y (0;{self.c})')
            if b != 0:
                if b:
                    x_0 = round(-c / b, 2)
                else:
                    x_0 = 0
                self.label_5.setText(f'Нули функции y = 0 при x = {x_0}')
            elif b == 0 and c == 0:
                self.label_5.setText(f'y = 0 при любом x')
            else:
                self.label_5.setText(f'Нулей не существует')
        x = np.linspace(-20, 20, 10000)
        fig, ax = plt.subplots()
        fig.set_size_inches(2, 2)
        ax.set_ylim(-20, 20)
        ax.set_xlim(-20, 20)
        fig.set_size_inches(5, 4)
        ax.grid()
        y = a * (x ** 2) + b * x + c
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlabel('Ось x', fontsize=14)
        plt.ylabel('Ось y', fontsize=14)
        plt.title('График', fontsize=14)
        fig.canvas.manager.window.move(515, 75)
        ax.plot(x, y)
        plt.show()

    def doo(self):
        plt.close()
        self.close()