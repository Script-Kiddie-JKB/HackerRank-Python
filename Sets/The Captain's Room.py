#author @Nishant

K = int(input())
roomNo = list(map(int, input().split()))

print(int(((sum(set(roomNo))*K - sum(roomNo))/(K-1))))