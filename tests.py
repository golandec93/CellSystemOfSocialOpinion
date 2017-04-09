import os

from src.utils import *
import src.dmanagement as dmn


def test_decorator(test):
    def decorated():
        res1 = "STARTING " + test.__name__
        stars = "*" * round(((72 - len(res1)) / 2))
        print(stars + res1 + stars)
        test()
        res1 = test.__name__ + " HAS BEEN SUCCESSFULLY EXECUTED"
        stars = "*" * round(((72 - len(res1)) / 2))
        print(stars + res1 + stars + "\n\n")

    return decorated


@test_decorator
def utils_test():
    opinion = get_from(array=(-1, 1), probabilities=(1 / 2, 1 / 2))
    if opinion != -1 and opinion != 1:
        raise Exception('so close :(')

    results = []
    a = (1, -1, 0)
    p = (1 / 3, 1 / 3, 1 / 3)
    for i in range(0, 1000):
        results.append(get_from(array=a, probabilities=p))
    plus = 0
    minus = 0
    null = 0

    for c in results:
        if c > 0:
            plus += 1
        elif c < 0:
            minus += 1
        elif c == 0:
            null += 1
    print("set = {0}\nprobabilities = {1}".format(a, p))
    print("plus: {0}\nminus: {1}\nnull: {2}".format(plus, minus, null))


@test_decorator
def save_test():
    cells = dmn.generate_radial_sample(5)
    file_path = dmn.get_current_date_and_time() + ".csv"
    dmn.save_to_csv(cells, file_path)
    loaded = dmn.load_cells_from_csv(file_path)
    for l, r in zip(cells, loaded):
        if l != r:
            raise Exception('not equals:\n{0}\n{1}'.format(l, r))
    os.remove(file_path)

utils_test()
save_test()
