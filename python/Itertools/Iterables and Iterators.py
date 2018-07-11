import itertools, math

number = int(input())
b = sorted(input().split())
ch = int(input())


lis = list(itertools.combinations(b,ch))
a=[]
for i in lis:
    if 'a' in i:
        a.append(i)
print(len(a)/len(lis))
