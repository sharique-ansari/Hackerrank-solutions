from collections import deque


def pile():
    while len(d) > 1:

        if d[0] == max(d):
            d.popleft()
        elif d[-1] == max(d):
            d.pop()
        else:
            return 'No'
    return 'Yes'


if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        n = input()
        d = deque(map(int, input().split()))
        print(pile())
