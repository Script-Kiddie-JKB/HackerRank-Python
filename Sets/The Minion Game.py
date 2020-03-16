#author @Nishant

def minion_game(string):
    n = len(string)
    stuart = 0
    kevin = 0
    for i in range(n):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            kevin += n - i
        else:
            stuart += n - i
    
    if stuart > kevin:
        print("Stuart "+str(stuart))
    elif kevin > stuart:
        print("Kevin "+str(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)