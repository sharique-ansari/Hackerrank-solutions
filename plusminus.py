#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(n, arr):
    a = 0
    b = 0
    c = 0
    for i in range(n):

        if arr[i] > 0:
            a += 1
        elif arr[i] < 0:
            b += 1
        else:
            c += 1
    print(format(float(a / n), ".6f"))
    print(format(float(b / n), ".6f"))
    print(format(float(c / n), ".6f"))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)
