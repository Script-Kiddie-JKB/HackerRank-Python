#author @Nishant

from itertools import combinations_with_replacement

x = input().split()
size = int(x[1])
x = list(x[0])
x.sort()
x = (list(combinations_with_replacement(x,size)))
for i in x:
    for j in i:
        print(j,end="")
    print()