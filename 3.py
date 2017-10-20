print 'Project Euler Problem 3\n'

num = 600851475143

def isPrime(x):
    if x == 1:
        val = False
    elif x == 2:
        val = True
    else:
        for i in range(2, x):
            if x % i == 0:
                val = False
                break
            else:
                val = True
    return val



factors= []

for i in range(1, 10000000):
    if num % i == 0:
        factors.append(i)

print factors

primeFactors = []
for k in factors:
    if isPrime(k):
        primeFactors.append(k)

print primeFactors


ans = raw_input('Press \'ENTER\' to close')
