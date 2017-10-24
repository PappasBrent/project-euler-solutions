import math

# Checks if a number is prime
def is_prime(x):
    if x < 0:
        x = abs(x)
    if x == 1 or x==0:
        return True
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
    return True

resultsArrays = []

# Loops through every possible value of a in the given parameters
for a in range(-1000, 1001):
    # Print a just so you know how far along you are
    print(a)
    # Loops through every possible value of b in the given parameters
    for b in range(-1000, 1001):

        # Defines f(x) as follows, which is the pattern for finding lots of primes
        def f(x):
            return x**2 + a * x + b

        # Starts k at 0, the lowest possible value
        k = 0
        # Creates an array of the range of the function f(x)
        results = []
        # While f(k) produces prime numbers, f(k) is appended to results
        # and k is increased. It's kind of like the Peter Principle
        while is_prime(f(k)):
            results.append(f(k))
            k += 1

        # Adds the values of a and b (stored as a tuple)
        # and the length of their range (how many consecutive
        # primes they produce) to the array of total results.
        resultsArrays.append(((a, b), len(results)))

# print(resultsArrays)

biggestPair = (0, 0)
biggestNumPrimes = 0

# Loops through the all the results and finds the result
# with the maximum number of consecutive primes and stores
# the values of a and b associated with it
for pair in resultsArrays:
    if pair[1] > biggestNumPrimes:
        biggestNumPrimes = pair[1]
        biggestPair = pair[0]
        print(biggestPair)


print("Largest number of consecutive primes:", biggestNumPrimes)
print("Pair used to obtain this value:", biggestPair)
print("Product of pair values:", biggestPair[0]*biggestPair[1])
