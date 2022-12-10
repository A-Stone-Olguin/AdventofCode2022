import re

#Import file
file = open("input.txt", "r")

lines = file.readlines()

# Update the cycleVal:
def updateCycle(cycle, cycleVal, x):
    #If our cycle is 20 or a multiple of 40 afterwards, add to our cycleVal
    if cycle == 20 or (cycle-20)%40 == 0:
        cycleVal.append(x*cycle)
    return cycleVal

#Initial conditions
x = 1
cycle = 0
#Array to store each cycle's value
cycleVal = []
#Go through each line
for line in lines:
    #Split for commands
    list = re.split(r'\s+', line)
    command = list[0]
    #If we modify x:
    if command == 'addx':
        #Get value
        val = int(list[1])
        #Increment cycle and update cycleVal
        cycle+= 1
        cycleVal = updateCycle(cycle, cycleVal, x)
        #Increment cycle and update cycleVal, then update x
        cycle+=1
        cycleVal = updateCycle(cycle, cycleVal, x)
        x += val
    else:
        #Increment cycle and update cycleVal
        cycle+=1
        cycleVal = updateCycle(cycle, cycleVal, x)

#Get the first six cycle vals, sum them up and print them
sum = 0
for i in range(6):
    sum += cycleVal[i]
print(sum)