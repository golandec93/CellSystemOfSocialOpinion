from math import pi
import matplotlib.pyplot as plt


def plot_current_state(cell_system):
    s = []
    for cell in cell_system.cells:
        s.append(cell.s)
    print("max(s) = {0}".format(max(s)))
    dot_sizer = 40 / max(s)

    for cell in cell_system.cells:
        if cell.opinion is 1:
            color = 'blue'
        else:
            color = 'red'
        plt.scatter(x=cell.x,
                    y=cell.y,
                    s=pi * cell.s * dot_sizer ** 2,
                    alpha=1 / 3,
                    c=color)
    plt.show()
