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
    opinion = get_from(array=(-1, 1), probabilities=(1 / 2, 1 / 2))
    if opinion != -1 and opinion != 1:
        raise Exception('so close :(')


utils_test()
