import re


def getSizes():
    #Open file
    file = open("input.txt", "r")
    #Get lines
    lines = file.readlines() 
    # Storing paths, directory names, and sizes
    dirPath = []
    currentDir = ''
    sizes = {}
    #Go through each line:
    for line in lines:
        #If we have command:
        if line[0] == '$':
            obj = re.split(r'\s', line)
            command = obj[1]
            # cd command
            if command == 'cd':
                if obj[2] == '..':
                    #Go back a path
                    oldDir = dirPath.pop()
                    currentDir = dirPath[-1]
                    #update the new currentDir
                    sizes[currentDir] += sizes[oldDir]
                elif obj[2] == '/':
                    # Only one call of this, start of file
                    currentDir = '/'
                    dirPath.append(currentDir)
                else:
                    # Have our current dir name be included in the path
                    currentDir = currentDir + '/' + obj[2]
                    # Add to path
                    dirPath.append(currentDir)
            #ls command
            else:
                # Initialize our value
                sizes[currentDir] = 0
                # else:
                    #same name dir, different path
                    # dirExists = True
                    # while dirExists:
                    #     currentDir = currentDir + '/'
                    #     if not (currentDir in sizes.keys()):
                    #         dirExists = False
                    # sizes[currentDir] = 0
        #Add files and dirs, from ls command output
        else :
            words = re.split(r'\s', line)
            num = 0
            # If we name a directory, don't add the size
            if words[0] == 'dir':
                num = 0
            # Add the file size
            else :
                num = int(words[0])
            sizes[currentDir] += num
    #After we are done, update with all the sizes:
    length = len(dirPath)
    # Go back and update the sizes one final time
    for i in range(length-1):
        oldDir = dirPath.pop()
        currentDir = dirPath[-1]
        sizes[currentDir] += sizes[oldDir]
    return sizes

# Function for finding all the directories with sizes <= 100000
def getSmallerSizes(sizes):
    # Initialize sum to 0
    sum = 0
    # Go through each directory
    for dir in sizes.keys():
        val = sizes[dir]
        # If our size is less than 100000, add it to our sum
        if val <= 100000:
            sum += val
    return sum
print(getSmallerSizes(getSizes()))
            
