from collections import deque


def stackup(a, b, k):
    for i in range(k):
        b1 = b.pop()
        if len(a) > 1:

            left = a.popleft()
            right = a.pop()
            if left > b1 and right > b1:
                return False
            elif left <= right <= b1:
                b.append(b1)
                b.append(right)
                a.appendleft(left)
            elif left <= b1:
                b.append(b1)
                b.append(left)
                a.append(right)
        elif len(a) == 1 and a.pop() <= b1:
            return True
        else:
            return False


if __name__ == '__main__':
    for i in range(int(input())):
        k = int(input())
        a = deque()
        a = deque(map(int, input().split()))
        b = [2147483649]
        print(stackup(a, b, k))
