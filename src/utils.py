from time import strftime, gmtime

from numpy.random import random
import numpy.random as np_rnd


def get_from(array, probabilities):
    return np_rnd.choice(a=array, p=probabilities)


def get_current_date_and_time(pattern='%Y-%m-%d_%H%M%S'):
    return strftime(pattern, gmtime())


urandom = random
