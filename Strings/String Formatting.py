#author @Nishant

def print_formatted(number):
    maxLen = len(str(bin(number))[2:])
    for i in range(1, number+1):
        dec = str(i)
        octal = str(oct(i))[2:]
        hexa = str(hex(i))[2:]
        binary = str(bin(i))[2:]
        hexa = hexa.upper()
        print('{:>{w}} {:>{w}} {:>{w}} {:>{w}}'.format(dec,octal,hexa,binary,w=maxLen))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)