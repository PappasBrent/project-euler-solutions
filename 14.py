def calc_chain_length(x):

    chainLength = 1

    while (x != 1):
        chainLength += 1
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
    return chainLength

maxChainLength = calc_chain_length(1)
maxChainNumber = 1

for i in range(1, 1000000):
    if (calc_chain_length(i) > maxChainLength):
        maxChainLength = calc_chain_length(i)
        maxChainNumber = i

print(maxChainNumber)
