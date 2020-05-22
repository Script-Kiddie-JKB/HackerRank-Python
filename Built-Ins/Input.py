#author @Nishant

x, k = map(int, input().split())
    expr = input()

    print(eval(expr) == k)