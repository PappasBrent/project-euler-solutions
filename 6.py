print 'Project Euler Problem 6\n'

num = 100

def sumSquare(x):
    val = 0
    for i in range(x+1):
        val+=(i**2)
    return val

def squareSum(x):
    val = 0
    for i in range(x+1):
        val+=i
    squareVal = val**2
    return squareVal

print(squareSum(num) - sumSquare(num))

ans = raw_input('Press \'ENTER\' to close')
