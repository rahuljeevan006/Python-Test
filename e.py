import math

dec = int(input('Enter the number of decimal places: '))
sum = 1
for i in range(1, dec+1):
    sum = sum + 1/math.factorial(i)
print ('Value =', round(sum, dec))

