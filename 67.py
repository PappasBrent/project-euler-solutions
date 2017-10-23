def get_children(tri, m, n):
    # Creates an empty list to store the children of the element
    # (The two elements directly below and adjacent to it)
    children = []
    #Tthe returned list contains the two elements directly
    # above and adjacent to the element in the triangle grid
    for i in range(2):
        children.append(tri[m + 1][n + i])
    return children


def get_parents(tri, m, n):
    # Creates an empty list to store the parent(s) of the element
    # (The two element(s) directly above and adjacent to it)
    parents = []
    # If the element is the first in the list, then it has only
    # one parent
    if n + 1 >= len(tri[m - 1]):
        return [tri[m - 1][n - 1]]
    # Otherwise, the returned list contains the two elements
    # directly above and adjacent to the element in the triangle grid
    for i in range(2):
        parents.append(tri[m - 1][n + i])
    return parents

# Dynamic method to calculate the maximum sum of a path of elements
# in a triangle grid


def get_max_path(tri):

    # Starts with the line just before the last line in the
    # triangle grid and continues until all lines have been
    # checked and replaced by their optimized pairings

    while len(tri) > 1:
        # Gets the current line in the grid whose values are to be checked
        currentLine = tri[-2]

        # Creates a variable to store the value of the new line
        # which will be replaced by its optimized values
        newLine = []

        # Goes through each value in the current line
        # and determines the value's largest child. Then,
        # the sum of the element and its largest child is
        # added to newLine as one of the optimized values
        for j in range(len(currentLine)):
            currentNum = currentLine[j]
            currentChildren = get_children(tri, -2, j)
            newLine.append(currentNum + max(currentChildren))
            # print(currentNum + max(currentChildren))

        # After determining all the optimized values for the current line,
        # the last line of the triangle is deleted and the line that was just
        # before it (which was the line that was just being checked) is
        # replaced by the newLine, which is the optimized pairings of these
        # two previous lines. newLine has a length of one less than that of
        # the last line in the triangle, which was just deleted.
        # Ultimately, the most optimized line will be all that's left,
        # and it will have a length of 1
        del tri[-1]
        tri[-1] = newLine

    return tri[0][0]

    while len(tri) > 1:
        currentLine = tri[-2]
        numWithBiggestChild = currentLine[0]
        biggestChild = get_children(tri, -2, 0)[0]

        newLine = []
        for j in range(len(currentLine)):
            currentNum = currentLine[j]
            currentChildren = get_children(tri, -2, j)
            # print(currentNum + max(currentChildren))
            newLine.append(currentNum + max(currentChildren))
        del tri[-1]
        tri[-1] = newLine

    return tri[0][0]

triangle = []

triangleFile = open("67.txt", "r")

for s in triangleFile.readlines():
    triangle.append(list(map(int, s.split())))

triangleFile.close()

print(get_max_path(triangle))
