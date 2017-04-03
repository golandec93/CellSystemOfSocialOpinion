from src.model import Cell
from src.utils import get_from
from math import sqrt
from src.utils import urandom


def generate_simple__random_cells(dots):
    x_coords = dots[0::2]
    y_coords = dots[1::2]
    cells = []
    cells_number = len(x_coords)
    for i in range(0, cells_number):
        cell = Cell(opinion=get_from(array=(-1, +1), probabilities=(1 / 2, 1 / 2)),
                    s=get_from(array=(1, 10), probabilities=(1 - 1 / (cells_number - 5), 1 / (cells_number - 5))),
                    b=1, x=x_coords[i], y=y_coords[i])
        cells.append(cell)
    return cells


def generate_radial_sample_dots(r, x_0, y_0):
    dots = []
    y = y_0 - r
    while y_0 - r <= y < y_0 + r:
        desc = (r - (y - y_0)) * (r + (y - y_0))
        left = int(x_0 - sqrt(desc))
        right = int(x_0 + sqrt(desc))
        x = left
        while left <= x <= right:
            # print(x,y)
            dots.append(x)
            dots.append(y)
            x += 1
        y += 1
    return dots


def generate_radial_sample():
    return generate_radial_sample(10)


def generate_radial_sample(radius):
    dots = generate_radial_sample_dots(radius, 10, 10)
    x_coords = dots[0::2]
    y_coords = dots[1::2]
    cells = []
    cells_number = len(x_coords)
    for i in range(0, cells_number):
        cell = Cell(opinion=get_from(array=(-1, +1), probabilities=(1 / 2, 1 / 2)),
                    s=urandom() * 5,
                    b=1, x=x_coords[i], y=y_coords[i])
        cells.append(cell)
    for cell in cells:
        if cell.x is 10 and cell.y is 10:
            cell.s = 30
    return cells
