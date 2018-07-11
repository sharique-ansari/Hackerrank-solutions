from collections import Counter

cShoe = int(input())
shoes = list(map(int, input().split()))
countShoe = Counter(shoes)
output = 0
for i in range(int(input())):
    sr = input().split()
    size = int(sr[0])
    r = int(sr[1])

    if countShoe[size] != 0:
        output += r
        countShoe[size] -= 1

print(output)
