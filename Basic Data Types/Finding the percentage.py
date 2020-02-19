n = int(input())
details = {}
for i in range (0,n):
    temp = input()
    temp = temp.split(" ")
    name = temp[0]
    m1 = float(temp[1])
    m2 = float(temp[2])
    m3 = float(temp[3])
    avg = (m1+m2+m3)/3.0
    details[name] = "%.2f"%avg
name = input()
print(details[name])