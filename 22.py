namesFile = open("p022_names.txt", "r")


# Creates a list out of all the names and removes the quotes between them
names = namesFile.read().split('","')
# Removes the first quote from the first name
names[0] = names[0][1:]
# Removes the last quote from the last name
names[-1] = names[-1][:-1]

# Sorts the names alphabetically
names.sort()

totalScore = 0

# Iterates through each name in the file

for i in range(len(names)):
    nameScore = 0
    # First finds the sum of the number values of each of the name's letters
    for letter in names[i]:
        nameScore += ord(letter) - 64
    # Then multiplies this value by the name's index in the list + 1
    nameScore *= (i + 1)
    totalScore += nameScore

print(totalScore)
