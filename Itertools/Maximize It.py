#author @Nishant
from itertools import product

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for i in range(K))
maxV = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(maxV))