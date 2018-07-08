#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ", "")
    l = len(s) ** 0.5
    out = ''
    rows = int(math.floor(l))
    column = int(math.ceil(l))
    for i in range(column):
        for j in range(rows):
            if j * column + i < len(s):
                out += s[j * column + i]
        out += ' '
    return out


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()
