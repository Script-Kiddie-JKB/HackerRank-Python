#author @Nishant

for i in range(int(input())):
    x = int(input())
    A = set(list(map(int, input().split())))
    x = int(input())
    B = set(list(map(int, input().split())))
    print(A<=B)