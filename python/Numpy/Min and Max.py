import numpy


if __name__ == '__main__':

    ab = list(map(int, input().split()))
    out = []
    for i in range(ab[0]):
        out.append(list(map(int, input().split())))
    print(numpy.max(numpy.min(out, axis=1)))
