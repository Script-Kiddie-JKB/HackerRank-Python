#author @Nishant

N = int(input())
m = 2*N-1
n = (2*N-1)+(2*N-2)
for i in range(1, n, 2):
    print(int((m-1*i)/2)*"-")