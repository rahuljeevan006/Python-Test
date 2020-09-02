n = int(input('Enter the no: '))

for i in range(2, n+1):
    if n % i == 0:
        isprime = 1
        for j in range(2,(i//2+1)):
            if(i % j == 0):
                isprime == 0
                break

        if(isprime == 1):
            print(i,'is a prime factor of', n)
