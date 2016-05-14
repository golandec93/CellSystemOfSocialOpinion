from numpy.random import random


def get_from(array, probabilities):
    probs = list(probabilities)
    probs[len(probs)-1] += 1
    r = random(1)

    upper_prob = probs[0]
    down_prob = 0

    for i in range(0, len(probs)):
        if down_prob <= r < upper_prob:
            return array[i]
        down_prob = upper_prob
        upper_prob += probs[i+1]
    return None
