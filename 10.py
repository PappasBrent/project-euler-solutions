print 'Project Euler Problem 5\n'

def isPrime(x):
    val = True
    if x == 1:
        val = False
    elif x == 2:
        val = True
    else:
        for k in range(2, x):
            if x % k == 0:
                val = False
                break
    return val

total = 0

for i in range(100):
    if isPrime(i):
        print i
        total +=i 

print total

ans = raw_input('Press \'ENTER\' to close')
