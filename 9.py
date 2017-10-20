from math import sqrt

print 'Project Euler Problem 9\n'

tripletFound= False

num = 500

triplets = []

theOneTripletToRuleThemAll = []

ans = 1

while (tripletFound == False):
    for i in range(300, num+1):
        for j in range(1, num):
            for k in range(1, j):
                if ((j**2) + (k**2)) == (i**2):
                    triplets.append([k, j, i])
                    print [k, j, i]
                    if i + j + k == 1000:
                        theOneTripletToRuleThemAll = [k, j, i]
                        tripletFound = True
                        break
        if tripletFound:
            break
                    
    num+=1

print theOneTripletToRuleThemAll

for dig in theOneTripletToRuleThemAll:
    ans *= dig

print ans

ans = raw_input('Press \'ENTER\' to close')
