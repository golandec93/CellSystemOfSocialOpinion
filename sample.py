from src.dmanagement import generate_radial_sample
from src.graphic import plot_current_state
from src.model import CellSystem
import numpy as np
import matplotlib.pyplot as plt

print("generating cell system")
cell_system = CellSystem(cells=generate_radial_sample(15),
                         social_temperature=50,
                         system_lobby_minus=-1,
                         system_lobby_plus=1,
                         measure=lambda cell, other_cell: np.hypot(cell.x - other_cell.x, cell.y - other_cell.y))

print("start cell system printing")
print("number of cells: {0}".format(len(cell_system.cells)))
print("number of positive adopters: {0}".format(cell_system.get_plus_adopters()))
plot_current_state(cell_system)

print("evaluating system adopters_evolution")
adopters_evolution = []
for i in range(0, 50):
    print(i)
    adopters_evolution.append(i)
    adopters_evolution.append(cell_system.get_plus_adopters())
    cell_system.evolve()
print("printing system adopters_evolution")
print(adopters_evolution[1::2])
plt.plot(adopters_evolution[0::2], adopters_evolution[1::2])
plt.show()
