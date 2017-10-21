goodNums = []

for i in range(2, 1000000):
    total = 0
    for num in str(i):
        total += int(num)**5
    if total == i:
        goodNums.append(i)

print(goodNums)

print(sum(goodNums))
