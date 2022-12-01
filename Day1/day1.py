## Read file
file = open("input.txt", "r")

#Maximum value
max = -1
#Sum variable
sum = 0
lines = file.readlines()
for line in lines: 
    #Check if line is empty
    if line.strip():
        sum += int(line)
    else :
        # find min
        if sum > max:
            max = sum 
            print(max)
        # reset sum
        sum = 0
print("Maximum is: " + str(max))