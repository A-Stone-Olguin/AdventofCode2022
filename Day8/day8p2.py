import re

#Open file
file = open("input.txt", "r")

#Get lines
lines = file.readlines() 

# Dicts for our "matrices"
rows = {}
columns = {}

##Make rows (original matrix)
rowInd = 0
for line in lines:
    nums = re.findall(r'\d+', line)

    list = []
    for i in range(len(nums[0])):
        # Adding into our matrix
        list.append(int((nums[0][i])))
    rows[rowInd] = list
    #Increasing our index
    rowInd += 1

##Make columns (transposed matrix)
for line in lines:
    nums = re.findall(r'\d+', line)

    list = []
    ##Adding columns
    for i in range(len(nums[0])):
        list.append(int((nums[0][i])))
        ## Make a new array for the column if it doesn't exist
        if not (i in columns.keys()):
            columns[i] = []
            columns[i].append(int(list[i]))
        ## Otherwise add to the row of the matrix
        else:
            columns[i].append(int(list[i]))



# Look to the right
def lookRight(rows, row, col):
    score = 0
    val = rows[row][col]
    for j in range(col, len(rows[row])-1):
        # Check if we can see
        if val > rows[row][j+1]:
            score += 1
        # Counting the tree we see last
        else:
            score+= 1
            break
    return score

# Look to the left
def lookLeft(rows, row, col):
    score = 0
    val = rows[row][col]
    # Reverse search
    list = rows[row]
    list.reverse()
    #Do the other direction, new starting point
    for j in range(len(list)-col-1, len(list)-1):
        # Check if we can see
        if val > list[j+1]:
            score += 1
        # Counting the tree we see last
        else:
            score+= 1
            break
    return score


# Look down
def lookDown(cols, row, col):
    score = 0
    val = cols[col][row]
    for j in range(row, len(cols[col])-1):
        # Check if we can see
        if val >cols[col][j+1]:
            score += 1
        # Counting the tree we see last
        else:
            score+= 1
            break
    return score

# Look up
def lookUp(cols, row, col):
    score = 0
    val = cols[col][row]
    # Reverse search
    list = cols[col]
    list.reverse()
    #Do the other direction, new starting point
    for j in range(len(list)-row-1, len(list)-1):
        # Check if we can see
        if val > list[j+1]:
            score += 1
        # Counting the tree we see last
        else:
            score+= 1
            break
    return score


## Calculate the score
score = 0
# Go through each possible starting point
for i in range(len(rows)):
    for j in range(len(rows[i])):
        newScore = 1
        # Multiply by each direction
        newScore *= lookRight(rows, i,j)
        newScore *= lookLeft(rows, i,j)
        newScore *= lookDown(columns, i,j)
        newScore *= lookUp(columns, i,j)
        # Update score if it is the best
        if newScore > score:
            score = newScore
#Print the final score
print(score)




