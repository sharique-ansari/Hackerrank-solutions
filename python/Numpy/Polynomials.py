import numpy

ll = list(map(float, input().split()))

print(numpy.polyval(ll, float(input())))
