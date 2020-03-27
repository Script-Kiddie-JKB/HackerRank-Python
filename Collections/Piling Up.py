#author @Nishant

for _ in range(int(input())):
    n = input()
    lst = list(map(int, input().split()))
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")