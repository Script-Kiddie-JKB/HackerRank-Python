#author @Nishant

n = int(input())
arr = map(int, input().split())

score = list(arr)
maxx = max(score)

score1 = []
for i in range(len(score)):
    if score[i] != maxx:
        score1.append(score[i])
maxx = max(score1)
print(maxx)