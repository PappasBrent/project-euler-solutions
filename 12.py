currentNum=250012
currentTri=0
numDivisors=0



while True:
    numDivisors=0
    currentTri+=currentNum
    currentNum+=1
    if currentTri % 2 == 0 and currentTri!=1:
        for i in range(1, int((currentTri+1)/2)):
            if currentTri % i == 0:
                numDivisors+=1
    else:
        continue
    numDivisors+=1
    print(currentTri, numDivisors)
    if numDivisors>250:
        break

print(currentTri, numDivisors)
