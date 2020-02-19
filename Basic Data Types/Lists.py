#author @Nishant

n = int(input())
arr = []
for i in range(0,n):
    temp = input()
    temp = temp.split(" ")
    command = temp[0]
    if command=="insert":
        arr.insert(int(temp[1]),int(temp[2]))
    elif command=="print":
        print(arr)
    elif command=="remove":
        arr.remove(int(temp[1]))
    elif command=="append":
        arr.append(int(temp[1]))
    elif command=="sort":
        arr.sort()
    elif command=="pop":
        arr.pop()
    elif command=="reverse":
        arr.reverse()