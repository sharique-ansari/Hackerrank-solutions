import numpy

ab = list(map(int, input().split()))
out = []
for i in range(ab[0]):
    out.append(list(map(int, input().split())))
print(numpy.prod(numpy.sum(out, axis=0)))




