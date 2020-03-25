#author @Nishant

from collections import namedtuple
n, colN = (int(input()), input().split()); Val = namedtuple('Val', colN)
marks = [int(Val._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks)/len(marks))