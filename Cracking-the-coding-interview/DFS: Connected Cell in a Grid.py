#!/bin/python3

import math
import os
import random
import re
import sys


# below code can be optimised further


def addNbr(i, j, grid):
    if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
        sum = 0
        grid[i][j] = 0
        visited[i][j] = 1

        sum += 1
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                sum += addNbr(k, l, grid)

        return sum
    return 0


def maxRegion(grid, n, m):
    max = -100000000

    for i in range(n):
        for j in range(m):
            if visited[i][j] != 1:

                a = addNbr(i, j, grid)
                if a > max:
                    max = a
    return max


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []
    visited = []
    for i in range(n):
        visited.append([0] * m)

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid, n, m)
    print(res)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
