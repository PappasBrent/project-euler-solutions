# I really liked this problem

import math


def calc_sum_divisors(n):
    sumDivisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # print(i, n/i)
            sumDivisors += i
            sumDivisors += (n / i)
        if i**2 == n:
            sumDivisors -= i

    sumDivisors -= n

    return int(sumDivisors)


total = 0

limit = 10000

sumsDivisors = {}
for i in range(limit):
    sumsDivisors[i] = calc_sum_divisors(i)

for a in range(1, limit):
    print(a)
    b = calc_sum_divisors(a)
    if calc_sum_divisors(a) == b and calc_sum_divisors(b) == a and a != b:
        total += a + b
        print(a, b)

total/=2

print(total)
