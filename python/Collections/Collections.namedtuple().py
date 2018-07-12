from collections import namedtuple

# below code does not use namedtuple

# a, b, sum = int(input()), input().split().index('MARKS'), 0
# for i in range(a):
#     sum += input().split()[b]
# print(sum / a)

a, out = int(input()), 0
students = namedtuple('student',' '.join(input().split()))
for i in range(a):
    student = students(*input().split())
    out += int(student.MARKS)
print(format(out/a, ".2f"))
