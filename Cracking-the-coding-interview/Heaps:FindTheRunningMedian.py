#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

if __name__ == '__main__':
    n = int(input())

    half1 = []
    half2 = []
    max = 10000000000000

    for _ in range(n):
        a_item = int(input())
        len1 = len(half1)
        len2 = len(half2)
        if len1 == len2:
            if a_item < max:
                heapq.heappush(half1, -a_item)
                print(float(-half1[0]))
            else:
                heapq.heappush(half2, a_item)
                print(float(half2[0]))
        elif len1 > len2:
            if a_item < max:
                heapq.heappush(half2, -heapq.heappushpop(half1, -a_item))

            else:
                heapq.heappush(half2, a_item)
            print((half2[0] - half1[0]) / 2)
        else:
            if a_item > max:
                heapq.heappush(half1, -heapq.heappushpop(half2, a_item))
            else:
                heapq.heappush(half1, -a_item)
            print((half2[0] - half1[0]) / 2)
        max = -half1[0]
