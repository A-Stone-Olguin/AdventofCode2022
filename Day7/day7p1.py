import re

#Open file
file = open("t.txt", "r")

#Get lines
lines = file.readlines() 



dirPath = []
currentDir = ''
sizes = {}

for line in lines:
    #If we have command:
    if line[0] == '$':
        obj = re.split(r'\s', line)
        command = obj[1]
        # cd command
        if command == 'cd':
            if obj[2] == '..':
                #Go back a path
                currentDir = dirPath.pop()
            elif obj[2] == '/':
                currentDir = '/'
                dirPath = []
                dirPath.append(currentDir)
            else:
                currentDir = obj[2]
                # Add to path
                dirPath.append(currentDir)
        #ls command
        else:
            if not (currentDir in sizes.keys()):
                sizes[currentDir] = 0
    #Add files and dirs, from ls command
    else :
        words = re.split(r'\s', line)
        num = 0
        if words[0] == 'dir':
            dirOrder[currentDir][words[1]] = {}
        else :
            num = int(words[0])
        sizes[currentDir] += num