#author @Nishant

str = input()
salnum = False
salpha = False
sdigit = False
slower = False
supper = False
for i in str:
    if(i.isalnum()):
        salnum=True
    if(i.isalpha()):
        salpha=True
    if(i.isdigit()):
        sdigit=True
    if(i.islower()):
        slower=True
    if(i.isupper()):
        supper=True
    
print(salnum)
print(salpha)
print(sdigit)
print(slower)
print(supper)