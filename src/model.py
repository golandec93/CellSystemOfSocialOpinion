from numpy.random import random
from math import exp


class Cell:
    def __init__(self, opinion=None, s=None, b=None, x=None, y=None):
        self.s = s
        self.b = b
        self.opinion = opinion
        self.y = y
        self.x = x


class CellSystem:
    def __init__(self, cells, social_temperature, system_lobby_plus, system_lobby_minus, measure):
        self.measure = measure
        self.system_lobby_minus = system_lobby_minus
        self.system_lobby_plus = system_lobby_plus
        self.social_temperature = social_temperature
        self.cells = cells

    def __next__(self):
        self.cells.__next__()

    def __iter__(self):
        self.cells.__iter__()

    def get_influence(self, cell):
        if cell.opinion > 0:
            lobby = self.system_lobby_plus
        else:
            lobby = self.system_lobby_minus
        influence = - cell.s * cell.b - cell.opinion * lobby
        for other_cell in self:
            if cell is other_cell:
                pass
            influence -= (other_cell.s * other_cell.opinion * cell.opinion) / self.measure(cell, other_cell)
        return influence

    def evolve(self):
        for cell in self:
            save_probability = 1 / (1 + exp((2 * self.get_influence(cell)) / self.social_temperature))
            r = random(1)
            if r <= save_probability:
                cell.opinion *= -1

    def get_plus_adopters(self):
        adopters = 0
        for cell in self:
            if cell.opinion > 0: adopters += 1
        return adopters

    def get_minus_adopters(self):
        adopters = 0
        for cell in self:
            if cell.opinion < 0: adopters += 1
        return adopters
