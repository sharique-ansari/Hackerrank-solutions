if __name__ == '__main__':
    n = input()
    setA = set(input().split())

    for i in range(int(input())):
        operation = input().split()[0]

        getattr(setA, operation)(set(input().split()))

    print(sum(map(int, setA)))
