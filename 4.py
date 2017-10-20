print 'Project Euler Problem 4\n'


def isPal(x):
    palVal = False
    var = str(x)
    if len(var) == 1:
        palVal = True
    else:
        for j in range(len(var)):
            if var[j] == var[len(var)-(1+j)]:
                palVal = True
            else:
                palVal = False
                break

    return palVal

palProducts = []
for x in range(100, 1000):
    for y in range(100, 1000):
        if isPal(x*y):
            palProducts.append(x*y)

print max(palProducts)

ans = raw_input('Press \'ENTER\' to close')
