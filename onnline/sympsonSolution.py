from function import distanceCoveredByRocket


def simpsonFunction(lowerBound, upperBound, n):
    h = (upperBound - lowerBound) / (2 * n)

    result = 0.0

    for i in range(0, n):
        c = lowerBound + (2 * h)

        result += ((h / 3) * (
                distanceCoveredByRocket(lowerBound) + 4 * distanceCoveredByRocket((lowerBound + c) / 2) + distanceCoveredByRocket(c)))

        lowerBound = c

    return result




