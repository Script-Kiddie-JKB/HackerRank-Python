#author @Nishant

import re

n = int(input())
for i in range(0,n):
    k = input()
    print (bool(re.match('^[+-]?\d*?\.{1}\d+$',k)))