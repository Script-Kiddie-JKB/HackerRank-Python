#author @Nishant

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Other method instead of using textwrap

#str = input()
#str_len = len(str)
#n = int(input())
#for i in range(0,str_len,n):
#    for j in range(0,n):
#        print(str[j],end="")
#    str = str[2:]
#   print()