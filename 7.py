print 'Project Euler Problem 7\n'

def isPrime(x):
    val = False
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



primes = []

num = 1

while (len(primes) < 10001):
    if isPrime(num):
        primes.append(num)
        print str(num) + "\t" + str(len(primes))
    num+=1


print ''
print primes[len(primes)-1]

ans = raw_input('Press \'ENTER\' to close')
