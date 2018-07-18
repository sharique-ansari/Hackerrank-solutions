from collections import OrderedDict

if __name__ == '__main__':
    dicts = OrderedDict()
    k = 0
    for i in range(int(input())):
        a = input()
        if a in dicts:
            dicts[a] += 1
        else:
            dicts[a] = 1
            k += 1
    print(k)
    for j in dicts:
        print(dicts[j], end=" ")
