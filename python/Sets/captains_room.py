if __name__ == '__main__':
    n = int(input())
    array = list(map(int,input().split()))
    sset = set(array)
    sum=0

    for k in array:
        sum+=k
    print(sum)
    sum2=0
    for i in sset:
        sum2+=i
    print(int((sum2*n-sum)/(n-1)))