#author @Nishant
import math
ab = int(input())
bc = int(input())
ans = round(math.degrees(math.atan(ab/bc)))
ans = str(ans)+'°'
print(ans)