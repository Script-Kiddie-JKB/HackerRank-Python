#author @Nishant

def average(array):
    #author @Nishant
    array = set(array)
    return sum(array)/len(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)