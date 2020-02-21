def merge_the_tools(string, k):
    SS = []
    tempLen = 0
    for i in string:
        tempLen += 1
        if i not in SS:
            SS.append(i)
        if tempLen==k:
            print (''.join(SS))
            SS = []
            tempLen = 0
                

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)