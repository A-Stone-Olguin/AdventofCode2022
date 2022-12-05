import re

#Open file
file = open("input.txt", "r")

#Get lines
lines = file.readlines() 

#Dict for each stack
stacks = {}
#Finding number of stacks and what line we count the number of stacks
stackNum = 0
index = 0

#Get number of stacks
for line in lines:
    #Get index of how many stacks:
    nums = re.findall(r'\d+', line)
    #Find where the stackNums start
    if(len(nums) >0) :
        stackNum = int(nums[len(nums)-1])
        break
    else :
        index += 1

#Getting the stacks:
for i in range(stackNum):
    stack = []
    for j in range(index):
        char = lines[j][i*4 +1]
        if char != ' ':
            stack.insert(0, char)
    stacks[i+1] = stack

# Read instructions
index += 2
for i in range(len(lines)-index):
    #Get the nums
    nums = re.findall(r'\d+', lines[i+index])

    #Rename the nums:
    numToMove = int(nums[0])
    fromMove = int(nums[1])
    toMove = int(nums[2])

    #Do the operations, moving one at a time  
    for j in range(numToMove):
        #Get char
        char = stacks[fromMove].pop()
        #Put in new stack
        stacks[toMove].append(char)

#Print top of each stack, and its number
for i in stacks.keys():
    print("Stack num " + str(i) + " Top letter " + stacks[i].pop())
        
