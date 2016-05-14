from src.dmanagement import generate_radial_sample_dots
import matplotlib.pyplot as plt
from src.model import CellSystem
from src.model import Cell
from math import sqrt, pi
from src.dmanagement import generate_simple_cells

print("start dots generation")
dots = generate_radial_sample_dots(10, 10, 10)
# print(dots)
x = dots[0::2]
y = dots[1::2]
dots_1 = zip(x, y)

'''for dot in dots_1:
    plt.scatter(dot[0], dot[1])
plt.show()
'''
print("start cell system generation")
cell_system = CellSystem(cells=generate_simple_cells(dots),
                         social_temperature=1,
                         system_lobby_minus=-1,
                         system_lobby_plus=1,
                         measure=lambda a, b : sqrt(a*a + b*b))

print("start cell system printing")
print("number of cells: {0}".format(len(cell_system.cells)))

s = []
for cell in cell_system.cells:
    s.append(cell.s)

dot_sizer = 40/max(s)


for cell in cell_system.cells:
    if cell.opinion is 1:
        color = 'blue'
    else:
        color = 'red'
    plt.scatter(x=cell.x,
                y=cell.y,
                s=pi*cell.s*dot_sizer**2,
                alpha=1/2,
                c=color)
plt.show()