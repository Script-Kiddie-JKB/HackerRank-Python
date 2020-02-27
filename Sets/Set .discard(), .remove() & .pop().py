#author @Nishant

n = int(input())
s = set(map(int, input().split()))

n = int(input())
for i in range(n):
    command = input()
    if(command == "pop"):
        s.pop()
    else:
        command = command.split()
        if(command[0] == "remove"):
            s.remove(int(command[1]))
        else:
            s.discard(int(command[1]))
print(sum(s))