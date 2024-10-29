# error check for quadratic formula
import math
a=1
b=5
c=4
delta = (b*b)-(4*(a*c))
if delta <0:
    print('Not real roots')
else:
    d = math.sqrt(delta)
    print((-b+d)/2*a)
    print((-b-d)/2*a)