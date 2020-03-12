#author @Nishant
from collections import Counter

x = int(input())

sSize = Counter(map(int, input().split()))

n = int(input())
earning = 0
for i in range(0,n):
    sWant, price = map(int, input().split())
    if(sSize[sWant]!=0):
        sSize[sWant] -= 1
        earning += price
print(earning)