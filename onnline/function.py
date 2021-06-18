import math


def distanceCoveredByRocket(t):
    return 2000 * math.log(140000 / (140000 - 2100 * t)) - 9.8 * t
