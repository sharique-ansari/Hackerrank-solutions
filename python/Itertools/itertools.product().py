if __name__ == '__main__':
    from itertools import product

    A,B = list(map(int, input().split())),list(map(int, input().split()))

    print(*list(product(A, B)), end=" ")
