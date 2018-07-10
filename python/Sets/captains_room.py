#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findLonely function below.
def findLonely(arr):
    sset = set(arr)
    sum = 0
    sum2 = 0
    for i in arr:
        sum += i
    for j in sset:
        sum2 += j
    return 2 * sum2 - sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = findLonely(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
