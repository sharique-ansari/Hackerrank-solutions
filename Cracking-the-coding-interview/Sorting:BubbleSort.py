#!/bin/python3

import math
import os
import random
import re
import sys


def countSwaps(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swaps += 1
        if not swapped:
            break
    print('Array is sorted in ' + str(swaps) + " swaps.")
    print('First Element: ' + str(arr[0]))
    print('Last Element: ' + str(arr[len(arr) - 1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
