#!/bin/python3

import math
import os
import random
import re
import sys

# this program is not complete, please don't run


# Complete the isValid function below.
def isValid(s):
    sets = set(s)
    i = sets
    dicts = {}
    cout = 0
    for i in sets:
        dicts[i] = count(s, i)
    print(sorted(dicts.values()))
    sset=set(dicts.values())
    print(sset)
    if len(sset)>2:
        return 'NO'
    elif len(sset)==1:
        return 'YES'
    a=sset.pop()
    b=sset.pop()
    print(a,b)
    # elif count(a,dicts.values()) ==1 or count(b,dicts.values())==1:






    return


def count(s, c):
    # Count variable
    res = 0

    for i in range(len(s)):

        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    # fptr.write(result + '\n')

    # fptr.close()
