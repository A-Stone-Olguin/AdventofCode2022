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



## Make a matrix for viewable trees (prevent double-counting)
def makeTrueFalseMatrix(rows, columns):
    tfMatrix = []
    for i in range(len(rows.keys())):
        tfMatrix.append([])
        for j in range(len(columns.keys())):
            #Initialize to all false
            tfMatrix[i].append('F')
    return tfMatrix


## Calculate the number of trees by counting trues
def calculateTrues(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'T':
                count += 1
    return count


# Go through rows, left to right:
def goThruRowsLR(rows, tfMatrix):
    for key in rows.keys():
        val = -1
        for i in range(len(rows[key])):
            # If viewable, fix matrix to have a true
            if val < rows[key][i] or i == 0:
                val = rows[key][i]
                tfMatrix[key][i] = 'T'
    return tfMatrix

# Go through rows, right to left:
def goThruRowsRL(rows, tfMatrix):
    for key in rows.keys():
        val = -1
        # Reverse the list to go the other way
        list = rows[key]
        list.reverse()
        for i in range(len(list)):
            # If viewable, fix matrix to have a true
            if val < list[i] or i == (len(list)-1):
                val = list[i]
                tfMatrix[key][len(list)-1-i] = 'T'
    return tfMatrix

# Go through cols Up to Down:
def goThruColsUD(columns, tfMatrix):
    for key in columns.keys():
        val = -1
        for i in range(len(columns[key])):
            # If viewable, fix matrix to have a true
            if val < columns[key][i] or i == 0:
                val = columns[key][i]
                # We are transposed, swap indices in true-false matrix
                tfMatrix[i][key] = 'T'
    return tfMatrix

# Go through cols Down to Up:
def goThruColsDU(columns, tfMatrix):
    for key in columns.keys():
        val = -1
        # Reverse the list to go the other way
        list = columns[key]
        list.reverse()
        for i in range(len(list)):
            # If viewable, fix matrix to have a true
            if val < list[i] or i == (len(list)-1):
                val = list[i]
                # We are transposed, swap indices in true-false matrix
                tfMatrix[len(list)-1-i][key] = 'T'
    return tfMatrix

# Initialize our True false matrix
tfMatrix = makeTrueFalseMatrix(rows, columns)
#Update true-false matrix for each direction
tfMatrix = goThruRowsLR(rows, tfMatrix)
tfMatrix = goThruColsUD(columns, tfMatrix)
tfMatrix = goThruColsDU(columns, tfMatrix)
tfMatrix = goThruRowsRL(rows, tfMatrix)

# Get our count of trues
count = calculateTrues(tfMatrix)

print(count)




