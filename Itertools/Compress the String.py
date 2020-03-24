#author @Nishant

from itertools import groupby

# x = input()

# groups = []
# uniquekeys = []

# for k, g in groupby(x, lambda x: x):
#     groups.append(list(g))      # Store group iterator as a list
#     uniquekeys.append(k)
# j = 0
# for i in groups:
#     print("(",len(i),",",uniquekeys[j],")")
#     j+

print(*[(len(list(c)), int(k)) for k, c in groupby(input())])
    