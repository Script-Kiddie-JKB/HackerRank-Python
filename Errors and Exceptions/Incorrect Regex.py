#author @Nishant

import re

for _ in range(int(input())):
    status = True
    try:
        regex = re.compile(input())
    except re.error:
        status = False
    print(status)