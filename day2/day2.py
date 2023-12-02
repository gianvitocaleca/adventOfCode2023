with open('day2.txt') as f:
    text = f.read()

lines = text.split("\n")

"""Part One"""
red = 12
green = 13
blue = 14

sumIDs = 0

for line in lines:
    gameID = int(line.split(":")[0].split(" ")[1])
    sets = line.split(": ")[1].split("; ")
    for set in sets:
        quantities = set.split(", ")
        for quantity in quantities:
            if 'red' in quantity and int(quantity.split(" ")[0]) > red:
                gameID = 0
            if 'blue' in quantity and int(quantity.split(" ")[0]) > blue:
                gameID = 0
            if 'green' in quantity and int(quantity.split(" ")[0]) > green:
                gameID = 0

    sumIDs = sumIDs + gameID

print(sumIDs)


"""Part Two"""
totalPower = 0
for line in lines:
    sets = line.split(": ")[1].split("; ")
    redquan=0
    bluequan=0
    greenquan=0
    for set in sets:
        quantities = set.split(", ")
        for quantity in quantities:
            if 'red' in quantity and int(quantity.split(" ")[0]) > redquan:
                redquan = int(quantity.split(" ")[0])
            if 'blue' in quantity and int(quantity.split(" ")[0]) > bluequan:
                bluequan = int(quantity.split(" ")[0])
            if 'green' in quantity and int(quantity.split(" ")[0]) > greenquan:
                greenquan = int(quantity.split(" ")[0])

    totalPower = totalPower + redquan*bluequan*greenquan

print(totalPower)
