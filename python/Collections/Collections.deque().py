from collections import deque

if __name__ == '__main__':
    dictionary = deque()

    for i in range(int(input())):
        ab = input().split()
        a = ab[0]

        try:
            b = int(ab[1])
        except IndexError:
            b = 0
        if a == 'append':
            dictionary.append(b)
        elif a == 'appendleft':
            dictionary.appendleft(b)
        elif a == 'pop':
            dictionary.pop()
        elif a == 'popleft':
            dictionary.popleft()
    print(*dictionary)
