#author @Nishant

from collections import defaultdict

A = defaultdict(list)

n, m = map(int, input().split())

for i in range(1,n+1):
    A[input()].append(i)

for i in range(m):
    print(' '.join(map(str, A[input()])) or -1)