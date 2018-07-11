#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the primality function below.

'''one more way to check for prime number is by Wilson's theorem 
    i.e check if (n-1)!\ \equiv\ -1 \pmod n 
    or  if (fact(n - 1) + 1) % n == 0 n is prime
'''


def primality(n):
    if (n % 2 == 0 and n != 2) or n == 1 or n % 3 == 0:
        return 'Not prime'
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return 'Not prime'
    return 'Prime'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())
    for p_itr in range(p):
        n = int(input())

        result = primality(n)
        # print(result)

        fptr.write(result + '\n')

    fptr.close()
