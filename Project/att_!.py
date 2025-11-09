import matplotlib.pyplot as plt
import numpy as np

# Создаем x значения
x_left = np.linspace(-3, -0.1, 300)
x_right = np.linspace(0.1, 3, 300)
x = np.concatenate([x_left, x_right])

# Разные параметры
hyperbolas = [
    {'k': 1, 'b': 0, 'color': 'blue', 'label': '$y = 1/x$'},
    {'k': 2, 'b': 0, 'color': 'red', 'label': '$y = 2/x$'},
    {'k': 1, 'b': 2, 'color': 'green', 'label': '$y = 1/x + 2$'},
    {'k': -1, 'b': 0, 'color': 'orange', 'label': '$y = -1/x$'}
]

plt.figure(figsize=(12, 8))

for hyp in hyperbolas:
    y = hyp['k'] / x + hyp['b']
    plt.plot(x, y, color=hyp['color'], linewidth=2, label=hyp['label'])

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.xlim(-3, 3)
plt.ylim(-8, 8)
plt.legend(fontsize=12)
plt.title('Семейство гипербол $y = k/x + b$')
plt.show()