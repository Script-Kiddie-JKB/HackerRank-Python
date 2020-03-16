#author @Nishant

A = set(list(map(int, input().split())))
N = int(input())

ans = True

for i in range(N):
    s = set(list(map(int, input().split())))
    if len(s) >= len(A):
        ans = False
        break
    if not s.issubset(A):
        ans = False

print(ans)