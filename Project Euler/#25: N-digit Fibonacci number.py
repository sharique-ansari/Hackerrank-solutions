from math import log10, ceil, sqrt

if __name__ == '__main__':

    phi = (1 + sqrt(5)) / 2

    a = int(input())
    for i in range(a):
        d = int(input())
        term = ceil((log10(5) / 2 + d - 1) / log10(phi))
        print(int(term))
