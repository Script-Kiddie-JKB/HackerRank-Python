#author @Nishant

from itertools import combinations

n = int(input())

x = list(input().split())
x.sort()
size = int(input())
count = 0
x = list(combinations(x,size))
for i in x:
    for j in i:
        if j=='a':
            count+=1
            break
print(count/len(x))