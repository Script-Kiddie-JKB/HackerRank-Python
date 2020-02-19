n = int(input())
x = input()
x = x.split(" ")
lst = []
for i in range(0,n):
    lst.append(int(x[i]))
tpl = tuple(lst)
print(hash(tpl))