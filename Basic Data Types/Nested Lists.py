#author @Nishant

n = int(input())
sheet = []
for i in range(n):
    temp = []
    name = input()
    marks = float(input())
    temp.append(name)
    temp.append(marks)
    sheet.append(temp)

scores = []
for i in range(len(sheet)):
    scores.append(sheet[i][1])

minn = min(scores)

scores1 = []
for i in range(len(scores)):
    if scores[i]!=minn:
        scores1.append(scores[i])

minn = min(scores1)

students = []
for i in range(len(sheet)):
    if minn == sheet[i][1]:
        students.append(sheet[i][0])
students.sort()
for i in range(len(students)):
    print(students[i])