def isPrime(num):
    if num == 2:
        return True
    for i in range(2, int((num // 2)+1)):
        if num % i == 0:
            return False
    return True

def nxtPrime(prime):
    nxt_prime = prime + 1
    while True:
        if not isPrime(nxt_prime):
            nxt_prime += 1
        else:
            break
    return nxt_prime

def question():
    prime = 2
    while True:
        ask = input('Should the next prime be printed')
        if ask == 'y':
            print(prime)
            prime = nxtPrime(prime)
        else:
            break

question()



