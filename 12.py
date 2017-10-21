import math

prevX = 0


def tri(x):
    return sum(range(x + 1))


def calc_num_divisors(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    numDivisors = 0
    if x % 2 == 0:
        for i in range(1, math.ceil(x / 2) + 1):
            if x % i == 0:
                numDivisors += 1
    else:
        for i in range(1, math.ceil(x / 3) + 1, 2):
            if x % i == 0:
                numDivisors += 1
    numDivisors += 1
    return numDivisors


# for i in range(10001):
#     print(i, calc_num_divisors(i))

for num in range(1, 10000, 15):
    print(num, tri(num), calc_num_divisors(tri(num)))
