def getidea(arr, a, b):
    setA = set(a)
    setB = set(b)
    hap = 0
    for i in arr:
        if i in setA:
            hap+=1
        elif i in setB:
            hap-=1
    return hap


if __name__ == '__main__':
    mn = input().split()
    n = mn[0]
    m = mn[1]
    arr = input().split()
    a = input().split()
    b = input().split()
    result = getidea(arr, a, b)
    print(result)
