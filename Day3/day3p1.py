import math


# Read file
file = open("input.txt", "r")

lines = file.readlines()

#Make priority
def makePrio() :
    # Create array
    vals = []
    for i in range(26):
        vals.append(chr(97+i))
    for i in range(26):
        vals.append(chr(65+i))
    return vals

#Get value of letter
def getVal(prio, char) :
    for i in range(len(prio)):
        if char == prio[i]:
            return i+1


def checkIn(chars, char):
    for i in range(len(chars)):
        if char == chars[i]:
            return True

sum = 0
for line in lines:
    # print(len(line))
    chars = []
    firstCompInd = math.floor(len(line)/2)
    for i in range(firstCompInd):
        chars.append(line[i])
    #check for matches
    for i in range(len(line)-firstCompInd):
        checkChar = line[firstCompInd + i] 
        if checkIn(chars, checkChar):
            sum += getVal(makePrio(), checkChar)
            break 
print(sum)


