import math

N = int(input('Enter the no of decimal digits needed'))

if N<50:
    print('%.*f' % (N, math.pi))
else:
    print('Number too large')
    N = int(input('Enter the no of decimal digits needed'))

