import sys
import math
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - 4*a*c
dd = d**0.5
x = (-b + dd)/(2*a)
y = (-b - dd)/(2*a)
print(int(x),"\r\n", int(y))