#author @Nishant

from itertools import combinations

x = input().split()
size = int(x[1])
x = list(x[0])
x.sort()
for k in range(1,size+1):
    final = (list(combinations(x,k)))
    for i in final:
        for j in i:
            print(j,end="")
        print()