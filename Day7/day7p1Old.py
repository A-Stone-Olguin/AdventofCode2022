import re

#Open file
file = open("t.txt", "r")

#Get lines
lines = file.readlines() 



dirPath = []

dirOrder = {}

sizes = {}





currentDir = ''
for line in lines:
    if line[0] == '$':
        obj = re.split(r'\s', line)
        command = obj[1]
        if command == 'cd':
            if obj[2] == '..':
                currentDir = dirPath.pop()
            else:
                currentDir = obj[2]
                dirPath.append(currentDir)
                dirOrder[currentDir] = {}
                # PathToDict(dirPath, dirOrder)
        else:
            if not (currentDir in sizes.keys()):
                sizes[currentDir] = 0
    #Add files and dirs
    else :
        words = re.split(r'\s', line)
        num = 0
        if words[0] == 'dir':
            dirOrder[currentDir][words[1]] = {}
        else :
            num = int(words[0])
        sizes[currentDir] += num
# print(sizes)
# print(dirOrder)
# print(dirOrder['/'])

# print(len(dirOrder['/']['a']))
# print(sizes['a'])

# Get sizes
def getSizes(name, dict):
    if len(dict[name]) == 0:
        # print(name)
        return sizes[name]
    else:
        num = 0
        print(dict)
        newDict = dict[name]
        for newName in newDict.keys():
            # print(newName)
            # print( newDict[newName])
            num += getSizes(newName, newDict)
        return num
test = getSizes('/', dirOrder)
print(test)
# print(dirOrder)
            
