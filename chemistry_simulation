import math

delta_H_zero = -813000
delta_S_zero = 156.90
delta_G_zero = -690000
T = float(input("insert the temperature during your experiment(in Kelvins)  "))
assert T >= 298 and T <= 553


def dG(T):
    dCP = 156.90 + 28.30 * T + -23.46 * T ** -2 - 8590.29974
    dH = -813000 + dCP * (T - 298)
    dS = 156.90 + math.log(T / 298)
    return dH - T * dS


dG(T)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

T = np.arange(298, 553, 0.001)
(dG,) = ax.plot(T, np.zeros_like(T), lw=2)


def submit(expression):
    """
    Update the plotted function to the new math *expression*.

    *expression* is a string using "T" as its independent variable, e.g.
    "T * 2".
    """
    ydata = eval(expression)
    dG.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    plt.draw()


axbox = fig.add_axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, "Evaluate")
text_box.on_submit(submit)
text_box.set_val("T * 2")  # Trigger `submit` with the initial string.

plt.show()

black.format_file_in_place('chem1.py', fast=False, mode=black.FileMode())
