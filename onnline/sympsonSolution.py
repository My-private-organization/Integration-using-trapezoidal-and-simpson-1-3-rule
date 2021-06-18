from function import distanceCoveredByRocket


def simpsonFunction(lowerBound, upperBound, division):

    h = (upperBound - lowerBound) / division

    newDivision = int(division / 2)

    result = 0

    for i in range(0, newDivision):

        c = lowerBound + (2 * h)

        result += ((h / 3) * (
                distanceCoveredByRocket(lowerBound) + 4 * distanceCoveredByRocket((lowerBound + c) / 2) + distanceCoveredByRocket(c)))

        lowerBound = c

    return result


n = int(input())

for j in range(1, n+1):
    print(simpsonFunction(8, 30, 2 * j))
