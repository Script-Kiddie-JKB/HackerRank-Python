#author @Nishant

from datetime import datetime as dt

for i in range(int(input())):
    print(int(abs((dt.strptime(input(), '%a %d %b %Y %H:%M:%S %z') - dt.strptime(input(), '%a %d %b %Y %H:%M:%S %z')).total_seconds())))