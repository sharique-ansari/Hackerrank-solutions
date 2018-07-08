#!/bin/python3

import os
import sys


#
# Complete the gradingStudents function below.
#
def gradingStudents(n, grades):
    for i in range(n):
        pres = grades[i]
        if pres < 38:
            grades[i] = pres
        elif ((pres // 5 + 1) * 5 - pres) < 3:
            grades[i] = ((pres // 5) + 1) * 5
    return grades

    #
    # Write your code here.
    #


if __name__ == '__main__':
    # use below line on hacker rank

    # f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(n, grades)
    print(result)

    # f.write('\n'.join(map(str, result)))
    # f.write('\n')
    # f.close()
