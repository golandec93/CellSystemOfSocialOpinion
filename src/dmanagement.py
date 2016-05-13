from src.model import Cell

def generate_simple_cells(dots):
    x_coords = dots[0::2]
    y_coords = dots[1::2]
    cells = []
    for x in x_coords:
        for y in y_coords:

            cells.append(Cell())