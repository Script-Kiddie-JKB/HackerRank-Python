#author @Nishant

from itertools import permutations

x = input().split()
size = int(x[1])
x = list(x[0])
x.sort()
x = (list(permutations(x,size)))
for i in x:
    for j in i:
        print(j,end="")
    print()