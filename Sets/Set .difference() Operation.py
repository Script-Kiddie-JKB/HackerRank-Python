#author @Nishant

n = int(input())
x = list(map(int, input().split()))
eng = set(x)
n = int(input())
x = list(map(int, input().split()))
frn = set(x)

print(len(eng.difference(frn)))