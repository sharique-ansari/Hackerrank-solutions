import numpy

if __name__ == '__main__':
    Anum = numpy.array(list(map(int, input().split())))
    Bnum = numpy.array(list(map(int, input().split())))

    print(numpy.inner(Anum, Bnum))
    print(numpy.outer(Anum, Bnum))