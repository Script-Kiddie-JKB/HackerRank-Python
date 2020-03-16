#author @Nishant

n = int(input())
A = set(list(map(int, input().split())))
n = int(input())
for i in range(0,n):
    inst, no = input().split()
    N = set(list(map(int, input().split())))
    getattr(A, inst)(N)

print(sum(A))