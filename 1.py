print 'Project Euler Problem 1\n'

total = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        print i
        total+=i

print ''
print total

ans = raw_input('Press \'ENTER\' to close')
