print 'Project Euler Problem 5\n'

def prime(x):
    val = 1
    for i in range(1, x+1):
        val *= i
    return val

minNum = 1

maxNum = 20

multiple = maxNum

multipleFound = False

multiples = []

if multiple % 2 != 0:
    multiple += 1

while (multipleFound == False):

    divisors= 0

    for j in range (minNum, maxNum + 1):
        if (multiple % j == 0):
            divisors += 1
            if divisors == maxNum:
                multiples.append(multiple)
                multipleFound = True
                break
        else:
            multiple+=2
            break

try:
    print (multiple)

except (ValueError):
    print ("Not high enough")

ans = raw_input('Press \'ENTER\' to close')
