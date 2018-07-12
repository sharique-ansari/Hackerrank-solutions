from collections import defaultdict

if __name__ == '__main__':

    gA, gB = list(map(int, input().split()))

    dedic = defaultdict(list)

    for i in range(gA):
        dedic[input()].append(i + 1)

    for j in range(gB):
        test = input()
        if test not in dedic:
            print(-1)
        else:
            print(*list(dedic[test]))
