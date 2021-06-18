from function import distanceCoveredByRocket


def multiSegmentTrapezoidal(a, b, n):
    h = (b - a) / n

    s = distanceCoveredByRocket(a) + distanceCoveredByRocket(b)

    i = 1
    while i < n:
        s += 2 * distanceCoveredByRocket(a + i * h)
        i += 1

    return (h / 2) * s


lowerBound = 8
upperBound = 30

previous = 0

n = int(input())

for i in range(1, n + 1):

    result = multiSegmentTrapezoidal(lowerBound, upperBound, i)

    if i == 1:
        print("Absolute approximate relative error for n = 1 is : " + "N/A")
    elif i <= 5:
        print("Absolute approximate relative error for n = %d is : %.4f" % (i, abs(result - previous) / result * 100))

    previous = result

print("Result from trapezoidal rule: ", "%.4f" % previous)
