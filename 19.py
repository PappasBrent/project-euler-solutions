firstDayOfYear = 2

monthStartsRegular = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
monthStartsLeapYear = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]

numSundaysOnFirsts = 0

for i in range(1901, 2001):
    numDays = 0
    isLeapYear = False
    if i % 4 == 0:
        if i % 100 != 0:
            isLeapYear = True
        else:
            if i % 400 == 0:
                isLeapYear = True

    # Adds 1 if it is a leapyear
    numDays = 365 + isLeapYear
    print(i, numDays)

    if isLeapYear:
        monthStartsThisYear = monthStartsLeapYear
    else:
        monthStartsThisYear = monthStartsRegular

    dayOfWeek = firstDayOfYear
    currentDay = 1
    while currentDay < numDays:
        if dayOfWeek == 7:
            if currentDay in monthStartsThisYear:
                numSundaysOnFirsts += 1
                print(currentDay)
        currentDay += 1
        dayOfWeek += 1
        if dayOfWeek > 7:
            dayOfWeek = 1

    firstDayOfYear += 1
    if firstDayOfYear > 7:
        firstDayOfYear = 1

print(numSundaysOnFirsts)
