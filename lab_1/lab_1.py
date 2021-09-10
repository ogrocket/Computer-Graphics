"""
Группа: М8О-308б-19
Студент: Степан Арапов
Номер лабораторной работы: 1
Вариант: 7
"""

# x = a*sin(t)
# y = b*cos(t)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

t = np.linspace(0, 2*np.pi, 100)
x = 1 * np.sin(t)
y = 1 * np.cos(t)

a_initial = '1'
b_initial = '1'

figure, ax = plt.subplots()
figure.subplots_adjust(bottom=0.2)
ax.set_title('x=a*sin(t), y=b*cos(t)')
ax.set_xlim(
    np.min(x) - (np.max(x)-np.min(x))/100,
    np.max(x) + (np.max(x)-np.min(x))/100
    )
ax.set_ylim(
    np.min(y) - (np.max(y)-np.min(y))/100,
    np.max(y) + (np.max(y)-np.min(y))/100
    )

l, = plt.plot(x, y)
l.set_ydata(y)
l.set_xdata(x)

def submit_a(a):
    x_new = float(a) * np.sin(t)
    l.set_xdata(x_new)
    ax.set_xlim(
        np.min(x_new) - (np.max(x_new)-np.min(x_new))/100,
        np.max(x_new) + (np.max(x_new)-np.min(x_new))/100
        )
    plt.draw()

def submit_b(b):
    y_new = float(b) * np.cos(t)
    l.set_ydata(y_new)
    ax.set_ylim(
        np.min(y_new) - (np.max(y_new)-np.min(y_new))/100,
        np.max(y_new) + (np.max(y_new)-np.min(y_new))/100
        )
    plt.draw()

axbox_a = plt.axes([0.13, 0.07,  0.4, 0.038])
text_box_a = TextBox(axbox_a, 'a: ', initial=a_initial)
text_box_a.on_submit(submit_a)

axbox_b = plt.axes([0.13, 0.02, 0.4, 0.038])
text_box_b = TextBox(axbox_b, 'b: ', initial=b_initial)
text_box_b.on_submit(submit_b)

plt.show()