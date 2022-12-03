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


sum = 0
groupCount = 0
chars = {}
#Go through each line
for line in lines:
    lineNum = groupCount%3
    #Get chars for each of the three lines
    chars[lineNum] = {}
    groupCount+= 1
    # Add chars for each line
    for char in line:
        if char in chars[lineNum].keys():
            chars[lineNum][char] += 1
        else:
            chars[lineNum][char] = 1
    #Every three lines:
    if groupCount%3 == 0:
        charCount = {}
        #Check and count each occurrence for each line
        for lineN in chars.keys():
            for char in chars[lineN]:
                if char in charCount.keys():
                    charCount[char] += 1
                else:
                    charCount[char] = 1
        #Determine which one had 3
        for key in charCount.keys():
            if charCount[key] == 3:
                sum+= getVal(makePrio(), key)
                chars = {}
                break




     
print(sum)


