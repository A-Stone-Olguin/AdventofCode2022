import re

#Open file
file = open("t.txt", "r")

#get buffer
buffer = file.readlines()
# print(buffer)

index = 0
chars = {}

for char in buffer:
    if index%4 == 0:
        chars[1] = char 
    elif index%4 == 1:
        chars[2] = char
    elif index%4 == 2:
        chars[3] = char
    elif index%4 == 3:
        chars[4] = char
    
    #check if the four are distinct
    dictCheck = {}
    for i in chars.keys():
        dictCheck[chars[i]] = i
    if len(dictCheck.keys()) == 4:
        break 
    else :
        index += 1
print(index+4)
    