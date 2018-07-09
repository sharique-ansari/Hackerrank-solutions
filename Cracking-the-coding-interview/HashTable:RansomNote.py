#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dic = {}
    for w in magazine:
        dic[w] = dic.get(w, 0) + 1
    for word in note:
        if dic[word] < 1:
            return 'NO'
        dic[word] -= 1
    return 'YES'


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
