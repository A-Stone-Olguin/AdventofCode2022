## Read file
file = open("input.txt", "r")

#CalTotals
CalTotals = []

#Sum variable
sum = 0
lines = file.readlines()
for line in lines: 
    #Check if line is empty
    if line.strip():
        sum += int(line)
    else :
        #Add sum to array
        CalTotals.append(sum)
        # reset sum
        sum = 0
#Now we are done, sort array, reverse order since we want top three
CalTotals.sort(reverse=True)

#Sum top 3 cals
sum = 0
for i in range(3):
    sum += CalTotals[i]
print(sum)