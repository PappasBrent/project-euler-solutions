import math

# prevX = 0

# OLD WAY!
# def tri(x):
#     return sum(range(x + 1))

#SMAT WAY!
def get_nth_tri(x):

    # Forget these, they all equal x...
    # a = x
    # b = x
    # c = x

    # What. I'm not sure why, but adding (1/2)a to the area
    # of the triangle yields the correct answer...
    # return (1 / 2) * a * b + ((1 / 2) * (a))
    # Simplify that... and return an int just because
    return int((1 / 2 * x) * (x + 1))


def calc_num_divisors(x):
    # Starts at 1, since every number is divisible by 1
    numDivisors = 1
    # Iterates up to the square root of the number
    for i in range(1, int(math.sqrt(x))+1):
        # If x is divisible by the current number i, then we know
        # That x is also divisible by the quotient of x and i.
        # E.g.: 36 / 2 = 18, so we know that 36 is divisible by by 2 and 18
        # and can add 2 to the number of Divisors
        # This conditional basically checks to see if the current number i
        # is the square root of x. If it is, then we only add 1 to the
        # number of divisors
        if x%i==0:
            if x/i!=x:
                numDivisors+=2
            else:
                numDivisors+=1
    return numDivisors



k=0
while calc_num_divisors(get_nth_tri(k)) <= 500:
        k+=1

print(k, get_nth_tri(k), calc_num_divisors(get_nth_tri(k)))


# Project Euler Solution

t = 1 # triangle number
a = 1
cnt = 0
while cnt  <= 500:
    cnt = 0
    a = a + 1
    t = t + a
    for i in range(1, int(math.sqrt(t)) + 1):
        if t % i == 0:
            cnt +=2
        if i**2==t:
            cnt-=1

print(t)
