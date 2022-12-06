#Open file
file = open("input.txt", "r")

# Get the single line
lines = file.readlines()
buffer = lines[0]

#Dict to stop duplication
chars = {}
#Go through all possible starts of buffers
for index in range(len(buffer)-3):
    #Make a dict to see if we have 14 unique elements
    dictCheck = {}
    for i in range(4):
        dictCheck[buffer[index+i]] = 1
    # If we have 4 keys, we have 14 unique 
    if len(dictCheck.keys()) == 4:
        print(index+4)
        break