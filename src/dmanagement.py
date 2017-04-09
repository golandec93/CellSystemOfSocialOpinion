from src.model import Cell
from src.utils import get_from, get_current_date_and_time
from src.utils import urandom
from functools import reduce
from math import sqrt
import csv


def generate_simple__random_cells(dots):
    x_coords = dots[0::2]
    y_coords = dots[1::2]
    cells_number = len(x_coords)
    cells = [Cell(opinion=get_from(array=(-1, +1), probabilities=(1 / 2, 1 / 2)),
                  s=get_from(array=(1, 10), probabilities=(1 - 1 / (cells_number - 5), 1 / (cells_number - 5))),
                  b=1, x=x_coords[i], y=y_coords[i])
             for i in range(0, cells_number)]
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
    cells_number = len(x_coords)
    cells = [Cell(opinion=get_from(array=(-1, +1), probabilities=(1 / 2, 1 / 2)), s=urandom() * 5, b=1, x=x_coords[i],
                  y=y_coords[i])
             for i in range(0, cells_number)]
    # sett central dot as leader
    next(filter(lambda cell: cell.x is 10 and cell.y is 10, cells)).s = 30
    return cells


def save_to_csv(cell_system, file_path=None):
    file_path = get_current_date_and_time() + '.csv' if file_path is None else file_path
    with open(file_path, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
        for cell in cell_system:
            writer.writerow([cell.x, cell.y, cell.b, cell.s, cell.opinion])
        csv_file.close()
        print('{} cells were saved to {}'.format(len(cell_system), file_path))


def load_cells_from_csv(file_path):
    with open(file_path, mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        cells = [Cell(x=float(row[0]), y=float(row[1]), b=float(row[2]), s=float(row[3]), opinion=int(row[4])) for row
                 in reader]
    print("total loaded {} from {}".format(len(cells), file_path))
    # print('cells:')
    # print(*cells, sep='\n')
    return cells
