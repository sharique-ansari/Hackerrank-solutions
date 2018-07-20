import numpy

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    for j in range(N):
        B.append(list(map(int, input().split())))
    A = numpy.array(A)
    B = numpy.array(B)
    print(A + B, A - B, A * B, A // B, A % B, A ** B, sep='\n')
