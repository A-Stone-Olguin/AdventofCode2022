import re






file = open("input.txt", "r")



lines = file.readlines()

containment = 0

for line in lines:
    assignments = re.split(r',', line)

    #Remove \n
    secondPart = re.split(r'\n', assignments[1])
    # print(secondPart)
    assignments[1] = secondPart[0]

    min = []
    max = []
    for i in range(2):
        nums = re.split(r'-', assignments[i])
        # print(nums)
        min.append(float(nums[0]))
        max.append(float(nums[1]))
    if min[0] <= min[1] and max[0] >= max[1]:
        containment += 1
    elif min[1] <= min[0] and max[1] >= max[0]:
        containment += 1
print(containment)