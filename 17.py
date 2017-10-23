singleDigits = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

tens = {
    "0": "ten",
    "1": "eleven",
    "2": "twelve",
    "3": "thirteen",
    "4": "fourteen",
    "5": "fifteen",
    "6": "sixteen",
    "7": "seventeen",
    "8": "eighteen",
    "9": "nineteen"
}

doubleDigits = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

"""
Only works for x <= 1000
"""


def int_to_word(x):

    if x == 1000:
        return("onethousand")

    s = str(x)

    word = ''

    if len(s) == 1:
        word += singleDigits[s]

    elif len(s) == 2:
        singleDigit = s[-1]
        tenDigit = s[-2]
        if tenDigit == "1":
            word += tens[singleDigit]
        else:
            word += doubleDigits[tenDigit]
            if singleDigit!="0":
                word += singleDigits[singleDigit]

    elif len(s) == 3:
        hundredDigit = s[-3]
        word += singleDigits[hundredDigit]
        word += "hundred"
        if s[1:] !="00":
            word += "and"
            word += int_to_word(int(s[1:]))

    return word

total=0

for i in range(1,1001):
    print(int_to_word(i))
    total+=len(int_to_word(i))

print(total)
