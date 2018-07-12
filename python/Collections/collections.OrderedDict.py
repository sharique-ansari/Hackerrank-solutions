from collections import OrderedDict

if __name__ == '__main__':
    dictionary = OrderedDict()
    for i in range(int(input())):
        item, _, cost = input().rpartition(" ")
        if item in dictionary:
            dictionary[item] += int(cost)
        else:
            dictionary[item] = int(cost)
    for j in dictionary:
        print(j, dictionary[j])
