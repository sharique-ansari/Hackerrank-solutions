from itertools import permutations

ak = input().split()
a = ak[0]
k = int(ak[1])
lis = list(permutations(a, 2))


for j in sorted(lis):
    print(*j, sep='')
