#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gameOfThrones function below.
def gameOfThrones(s):
    l = len(s)
    listl = []
    for i in s:
        if i not in listl:
            listl.append(i)
        else:
            listl.remove(i)
    if l % 2 == 0 and len(listl) == 0:
        return 'YES'
    elif l % 2 != 0 and len(listl) == 1:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
