#author @Nishant

from collections import OrderedDict

d = OrderedDict()
for _ in range(int(input())):
    item = input()
    quantity = 1
    d[item] = d.get(item, 0) + quantity
print(len(d))
for item, quantity in d.items():
    print(quantity, end=" ")