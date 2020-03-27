#author @Nishant

from collections import OrderedDict

s = input()
d = dict()
for i in range(len(s)):
    if (s[i] in d):
        d[s[i]] = d[s[i]] + 1
    else:
        d[s[i]] = 1

d_keys = list(d.values())
d_keys.sort(reverse = True)
d_keys = list(OrderedDict.fromkeys(d_keys[:3]))

count = 0
for i in range(len(d_keys)):
    list = [key for key,value in d.items() if value == d_keys[i]]
    if (len(list) > 1):
        list.sort()
    for j in range(len(list)):
        if(count < 3):
            print("{} {}".format(list[j],d[list[j]]))
            count = count + 1
        else:
            break