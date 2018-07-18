import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':

    ab = list(map(int, input().split()))
    matA = []
    matB = []
    for i in range(ab[0]):
        matA.append(list(map(int, input().split())))
    for j in range(ab[0]):
        matB.append(list(map(int, input().split())))

    print(numpy.dot(matA, matB))
