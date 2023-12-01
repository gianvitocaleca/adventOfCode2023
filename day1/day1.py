with open('day1.txt') as f:
    text = f.read()

lines = text.split("\n")

"""Part One"""
sumValues = 0
for line in lines:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
    first = int(digits[0])
    last = int(digits[-1])
    num = first*10 + last
    sumValues = sumValues + num

print(sumValues)

"""Part Two"""
toFind = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
          'eight', 'nine', 'zero']

numbers = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '0': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'zero': 0
}

sumValues = 0

for line in lines:
    digits = []
    substrings = [line[i: j] for i in range(len(line))
                  for j in range(i + 1, len(line) + 1)]

    for s in substrings:
        if s in toFind:
            digits.append(s)

    first = numbers[digits[0]]
    last = numbers[digits[-1]]
    num = first * 10 + last
    sumValues = sumValues + num

print(sumValues)
