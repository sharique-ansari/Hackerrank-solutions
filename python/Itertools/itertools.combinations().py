from itertools import combinations

ak = input().split()
a= sorted(ak[0])
k = int(ak[1])

for i in range(1,k+1):
    for l in list(combinations(a,i)):
        print(*l,sep='')