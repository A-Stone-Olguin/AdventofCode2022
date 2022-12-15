import re
import math



#Get the monkey data from the input
def getMonkeyData() :
    #Import file
    file = open("t.txt", "r")

    lines = file.readlines()


    #Get data from input:
    monkeys = {}
    for line in lines:
        checkMonkey = re.findall(r'Monkey', line)
        #If our line has monkey
        if len(checkMonkey) != 0:
            digitStr = re.search(r'\d+', line)
            monkeyNum = int(digitStr.group())
            monkeys[monkeyNum] = {}
            monkeys[monkeyNum]['inspCount'] = 0
        # Add to our current Monkey:
        
        #Add starting items' worry level
        checkStart = re.findall(r'Start', line)
        if len(checkStart) != 0:
            #Get all worry levels
            startingWorry = re.findall(r'\d+', line)
            #Making a list of our starting items for monkey
            startingItems = []
            for i in range(len(startingWorry)):
                startingItems.append(int(startingWorry[i]))
            monkeys[monkeyNum]['Items'] = startingItems
        #Add operation:
        checkOp = re.findall(r'Operation', line)
        if len(checkOp) != 0:
            opStr = re.split(r'= ', line)
            ops = re.split(r'\s+', opStr[1])
            #Removing newline
            newops = []
            for i in range(3):
                newops.append(ops[i])
            monkeys[monkeyNum]['Operation'] = newops 

        #Add Test:
        checkTest = re.findall(r'Test', line)
        if len(checkTest) != 0:
            monkeys[monkeyNum]['TestTF'] = {}
            modStr =  re.search(r'\d+', line)
            modOp = int(modStr.group())
            monkeys[monkeyNum]['TestTF']['Test'] = modOp
        #Add if true, false
        checkTrue = re.findall(r'true', line)
        if len(checkTrue) != 0:
            trueStr =  re.search(r'\d+', line)
            trueMonkey = int(trueStr.group())
            monkeys[monkeyNum]['TestTF']['true'] = trueMonkey
        
        checkFalse = re.findall(r'false', line)
        if len(checkFalse) != 0:
            falseStr =  re.search(r'\d+', line)
            falseMonkey = int(falseStr.group())
            monkeys[monkeyNum]['TestTF']['false'] = falseMonkey
    return monkeys

#Operation:
def doOperation(opList, old):
    #Get first and second op val:
    val = []
    for i in range(2):
        if opList[i*2] == 'old':
            val.append(old)
        else:
            val.append(int(opList[i*2]))
    #Get operation and do the op
    op = opList[1]
    if op == '+':
        return val[0] + val[1]
    elif op == '-':
        return val[0] - val[1]
    elif op == '*':
        return val[0] * val[1]
    elif op == '/':
        return val[0] // val[1]
    


#Inspect for all monkeys for a round
def oneRound(monkeys):
    #All monkeys go:
    for monkeyNum in monkeys.keys():
        #For each item in list:
        for item in range(len(monkeys[monkeyNum]['Items'])):
            #Increase inspection
            monkeys[monkeyNum]['inspCount'] += 1
            #Do operation on worry level:
            val = monkeys[monkeyNum]['Items'].pop()
            val = doOperation(monkeys[monkeyNum]['Operation'], val)
            #Worry level management:

            #Do test
            TFDict = monkeys[monkeyNum]['TestTF']
            testMod = TFDict['Test']
            trueMonkey = TFDict['true']
            falseMonkey = TFDict['false']
            if val % testMod == 0:
                #Add to true case monkeylist
                monkeys[trueMonkey]['Items'].append(val)
            else:
                monkeys[falseMonkey]['Items'].append(val)
    return monkeys


#Get gcd of list of ints
def multGcd(list):
    gcd = math.gcd(list[0], list[1])
    for i in range(2, len(list)):
        gcd = math.gcd(gcd, list[i])
    return gcd


monkeys = getMonkeyData()

# print(oneRound(monkeys))

#Do twenty rounds:
for i in range(20):
    monkeys = oneRound(monkeys)

#Get all inspection counts:
inspections = []
for monkey in monkeys.keys():
    inspections.append(monkeys[monkey]['inspCount'])
print("inspections: " + str(inspections))

#Print tests:
tests = []
for monkey in monkeys.keys():
    tests.append(monkeys[monkey]['TestTF']['Test'])
print("Tests: " + str(tests))

#Get top two monkeys:
inspections.sort(reverse = True)

#Get monkey business
monkeyBusiness = inspections[0]*inspections[1]
print(monkeyBusiness)