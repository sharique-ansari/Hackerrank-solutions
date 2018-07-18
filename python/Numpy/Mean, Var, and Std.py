import numpy
numpy.set_printoptions(legacy='1.13')
if __name__ == '__main__':

    ab = list(map(int, input().split()))
    out = []
    for i in range(ab[0]):
        out.append(list(map(int, input().split())))
    print(numpy.mean(out, axis=1))
    print(numpy.var(out, axis=0))
    print(numpy.std(out))
