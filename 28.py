width = 1001
height = 1001

grid = [[0 for x in range(width)] for y in range(height)]


def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(i, end='\t')
        print()
    print()


# print_matrix(grid)

startingY = int(height / 2)
startingX = int(width / 2)

currentY = startingY
currentX = startingX

maxMovesHorizontal = 1
maxMovesVertical = 1

currentVal = 1

grid[currentY][currentX] = currentVal

currentVal += 1

while True:

    try:

        for i in range(1, maxMovesHorizontal + 1):
            currentX += 1
            grid[currentY][currentX] = currentVal
            currentVal += 1
        maxMovesHorizontal += 1
        for j in range(1, maxMovesVertical + 1):
            currentY += 1
            grid[currentY][currentX] = currentVal
            currentVal += 1
        maxMovesVertical += 1

        for i in range(1, maxMovesHorizontal + 1):
            currentX -= 1
            grid[currentY][currentX] = currentVal
            currentVal += 1
        maxMovesHorizontal += 1
        for j in range(1, maxMovesVertical + 1):
            currentY -= 1
            grid[currentY][currentX] = currentVal
            currentVal += 1
        maxMovesVertical += 1

    except:
        break


initialVal = grid[0][0]
for num in grid[0]:
    num = initialVal
    initialVal += 1


# print_matrix(grid)

y = 0
x = 0

total=0

while(y < height and x < width):
    total+=grid[y][x]
    y+=1
    x+=1

y = height - 1
x = 0

while(y > -1 and x < width):
    total+=grid[y][x]
    y-=1
    x+=1

total-=1

print(total)