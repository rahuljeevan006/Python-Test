from random import randrange

n = int(input('Enter no of times the coin should be tossed: '))
h = 0
t = 0

for i in range (1, n+1):
    s = randrange(2)
    if s == 0:
        h += 1
    else:
        t += 1

print('Head:- ',h)
print('Tail:- ',t)

