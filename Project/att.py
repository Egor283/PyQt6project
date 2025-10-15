import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
a, b, c = int(input('Введите коэфициент a: ')), int(input('Введите коэфициент b: ')), int(input('Введите коэфициент c: '))
ax.set_ylim(-20, 20)
ax.set_xlim(-20, 20)
ax.grid()
x = np.linspace(-20, 20, 100)
y = a * x ** 2 + b * x + c
plt.xlabel(' Ось x', fontsize=14)
plt.ylabel('Ось y', fontsize=14)
plt.title('График', fontsize=14)
ax.plot(x, y)
#fig.savefig('Grafick.svg')
plt.show()