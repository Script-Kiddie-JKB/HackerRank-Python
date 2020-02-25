#author @Nishant

from collections import Counter

x = input()
n, m = x.split()

x = input()
x = list(map(int,x.split()))
x_count = Counter(x)

s1 = input()
s1 = set(x) & set(map(int,s1.split()))

s2 = input()
s2 = set(x) & set(map(int,s2.split()))
factor = 0
for i in s1:
    factor += x_count[i]

for i in s2:
    factor -= x_count[i]

print(factor)