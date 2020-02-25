#author @Nishant

n = int(input())
n = input()
n = map(int,n.split(" "))
n = set(n)

m = int(input())
m = input()
m = map(int,m.split(" "))
m = set(m)

ans = set()
ans = n.difference(m)
ans1 = m.difference(n)
lst = list(ans.union(ans1))
lst.sort()
for i in lst:
    print(i)