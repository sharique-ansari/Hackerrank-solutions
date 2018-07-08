#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nmq = input().split()

    n = int(nmq[0])

    m = int(nmq[1])

    q = int(nmq[2])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    dict = {}

    for q_itr in range(q):
        r1C1R2C2 = input().split()

        r1 = int(r1C1R2C2[0])

        c1 = int(r1C1R2C2[1])

        r2 = int(r1C1R2C2[2])

        c2 = int(r1C1R2C2[3])

        listl = []

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                st = str(a[i]) + '*' + str(b[j])
                if st in dict:
                    if dict[st] not in listl:
                        listl.append(dict[st])

                else:
                    dict[st] = math.gcd(a[i], b[j])
                    if dict[st] not in listl:
                        listl.append(dict[st])
        print(len(listl))
        # Write Your Code Here
