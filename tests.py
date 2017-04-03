from src.utils import *


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
    opinion = get_from(array=(-1, 1, 0), probabilities=(1 / 2, 1 / 2))
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
        elif c is 0:
            null += 1
    print("set = {0}\nprobabilities = {1}".format(a, p))
    print("plus: {0}\nminus: {1}\nnull: {2}".format(plus, minus, null))


#utils_test()
