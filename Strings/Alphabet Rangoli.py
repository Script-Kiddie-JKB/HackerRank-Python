#author @Nishant

N = int(input())
n = (2*N-1)+(2*N-2)
for i in range(1, N):
    m = 2*i-1
    str = ''
    value = 97+N-1
    for i in range(0,m):
        if i!=0:
            str += '-'
        str += chr(value)
        if(i<(m-1)/2):
            value -= 1
        else:
            value += 1
    print(str.center(n,'-'))

for i in range(N, 0, -1):
    m = 2*i-1
    str = ''
    value = 97+N-1
    for i in range(0,m):
        if i!=0:
            str += '-'
        str += chr(value)
        if(i<(m-1)/2):
            value -= 1
        else:
            value += 1
    print(str.center(n,'-'))