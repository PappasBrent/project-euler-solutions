print('Project Euler Problem 2\n')

x = 1
termVal = 0
total = 0

while termVal < 4000000:
    termVal+=x
    if termVal < 3:
        x = 1
    else:
        x = termVal-x
    # print(termVal)
    if termVal % 2 == 0:
        total+=termVal

print()
print(total)

ans = input('Press \'ENTER\' to close')
