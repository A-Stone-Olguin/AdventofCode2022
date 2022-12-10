import re

#Import file
file = open("input.txt", "r")

lines = file.readlines()

# Update cycle each time, check
def cycleUpdate(cycle, cycleVal, x):
    #Add a new row if we reach mod 40
    if (cycle)%40 == 0:
        cycleVal.append([])
    #If our val is within one of the cycle, we write #
    if abs(cycle%40 - x) <= 1:
        cycleVal[cycle//40].append('#')
    #Otherwise write a .
    else :
        cycleVal[cycle//40].append('.')
    return cycleVal


#Initial conds:
x = 1
cycle = 0
#Initial the pixels
cycleVal = []
cycleVal.append([])
cycleVal[0].append('#')
#Go through each command
for line in lines:
    # Split commands on space
    list = re.split(r'\s+', line)
    command = list[0]
    #If we have to modify x
    if command == 'addx':
        #Get value to modify
        val = int(list[1])
        #Increase cyle and update it
        cycle+= 1
        cycleVal = cycleUpdate(cycle, cycleVal, x)
        #Increase cycle, change x val, update cycleVal
        cycle+=1
        x += val
        cycleVal = cycleUpdate(cycle, cycleVal, x)
    else:
        #Increase cycle and update cycleVal
        cycle+=1
        cycleVal = cycleUpdate(cycle, cycleVal, x)

#Print our values
for i in range(len(cycleVal)):
    print(' '.join(cycleVal[i]))
