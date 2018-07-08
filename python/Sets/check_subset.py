


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a = int(input())
        setA = set(input().split())
        b = int(input())
        setB = set(input().split())
        if len(setA.difference(setB)) == 0:
            print('YES')
        else:
            print('NO')
