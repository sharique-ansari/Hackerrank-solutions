#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the stepPerms function below.
def stepPerms(n):
    if dict[n] != -1:
        return dict[n]
    else:
        global sum

        if n < 0:
            return 0
        else:
            return stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())
    global dict
    dict = [-1] * 40
    dict[1]=1
    dict[2]=2
    dict[3]=4
    for i in range(4,38):
        dict[i]=stepPerms(i)

    for s_itr in range(s):
        n = int(input())
        sum = 0
        if dict[n] != -1:
            res = dict[n]
        else:

            res = stepPerms(n)
            dict[n] = res
        # print(res)

        fptr.write(str(res) + '\n')

    fptr.close()
