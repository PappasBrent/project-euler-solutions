wordsFile = open("p042_words.txt", "r")

words = wordsFile.read().split('","')

words[0] = words[0][1:]
words[-1] = words[-1][:-1]


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


numTriWords = 0

triNums = list(map(get_nth_tri, range(1, 1000)))

for word in words:
    wordNum=0
    for letter in word:
        wordNum+=ord(letter)-64
    if wordNum in triNums:
        numTriWords+=1

print(numTriWords)
