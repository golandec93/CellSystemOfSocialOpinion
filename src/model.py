from math import exp
import numpy.random as nprnd


class Cell:
    def __init__(self, opinion=None, s=None, b=None, x=None, y=None):
        self.s = s
        self.b = b
        self.opinion = opinion
        self.y = y
        self.x = x

    def __format__(self, format_spec):
        return self.__str__()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'x={0}, y={1}, s={2}, b={3}, opinion={4}'.format(self.x, self.y, self.s, self.b, self.opinion)

    def __eq__(self, other):
        return True if self.x == other.x \
                       and self.y == other.y \
                       and self.b == other.b \
                       and self.opinion == other.opinion \
                       and self.s == other.s \
            else False


class CellSystem:
    def __init__(self, cells, social_temperature, system_lobby_plus, system_lobby_minus, measure):
        self.measure = measure
        self.system_lobby_minus = system_lobby_minus
        self.system_lobby_plus = system_lobby_plus
        self.social_temperature = social_temperature
        self.cells = cells
        self.old_opinions = {}
        self._update_opinions_history()

    def __next__(self):
        return self.cells.__next__()

    def __iter__(self):
        return self.cells.__iter__()

    def __getitem__(self, item):
        return self.cells[item]

    def __len__(self, other):
        return self.cells.__len__()

    def get_influence(self, cell):
        lobby = self.system_lobby_plus if cell.opinion > 0 else self.system_lobby_minus
        influence = - cell.s * cell.b - self.old_opinions[cell] * lobby
        for other in self:
            if cell is not other:
                influence -= (other.s * self.old_opinions[other] * self.old_opinions[cell]) / self.measure(cell, other)
        return influence

    def evolve(self):
        for cell in self:
            save_probability = 1 / (1 + exp((2 * self.get_influence(cell)) / self.social_temperature))
            change_probability = 1 - save_probability
            cell.opinion *= nprnd.choice(a=[1, -1],
                                         p=[save_probability, change_probability])
        self._update_opinions_history()

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

    def _update_opinions_history(self):
        for cell in self:
            self.old_opinions[cell] = cell.opinion
