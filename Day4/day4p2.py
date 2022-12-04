import re

#Import file
file = open("t.txt", "r")


#Go through lines
lines = file.readlines()

#Initialize output
containment = 0

#Go through each line:
for line in lines:
    #Split into two assignments
    assignments = re.split(r',', line)

    #Remove \n
    secondPart = re.split(r'\n', assignments[1])
    assignments[1] = secondPart[0]

    # Initialzing the mins and maxes of both
    min = []
    max = []
    #Go through each assignment:
    for i in range(2):
        # Get the numbers:
        nums = re.split(r'-', assignments[i])
        #Add the numbers to min and max
        min.append(float(nums[0]))
        max.append(float(nums[1]))
    #Do comparisons, each determines an overlap
    if min[1] <= max[0] and min[0] <= min[1]:
        containment += 1
    elif min[0] <= max[1] and min[1] <= min[0]:
        containment += 1
# Print answer
print(containment)