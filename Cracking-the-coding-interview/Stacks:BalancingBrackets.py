#!/bin/python3

import math
import os
import random
import re
import sys

dict = {'(': ')', '{': '}', '[': ']', '#': '#', ']': 1, '}': 2, ')': 3}


def evaluate(exp):
    stack = ['#']
    for i in exp:
        a = stack.pop()
        if not dict[a] == i:
            stack.append(a)
            stack.append(i)
    if stack.pop() == '#':
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        expression = input()
        result = evaluate(expression)
        print(result)
