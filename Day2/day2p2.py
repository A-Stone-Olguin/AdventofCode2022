elfDict = {"A" : "Rock",
           "B" : "Paper",
           "C" : "Scissors"}

MyDict  = {"X" : "Lose",
           "Y" : "Draw",
           "Z" : "Win"}

##Score for using rsp
rspVals = {"Rock"      : 1,
           "Paper"     : 2,
            "Scissors" : 3}

## Getting win/loss/tie score
def rspwlt (elf, me) :
    if elf == me :
        return 3
    elif elf == "Rock" :
        if me == "Paper":
            return 6
        else :
            return 0
    elif elf == "Paper":
        if me == "Scissors":
            return 6
        else :
            return 0
    else :
        if me == "Rock":
            return 6
        else :
            return 0

def getResponse(elf, condition) :
    if condition == "Draw" :
        return elf 
    elif condition == "Win" :
        if elf == "Rock" :
            return "Paper"
        elif elf == "Paper":
            return "Scissors"
        else:
            return "Rock"
    else :
        if elf == "Rock" :
            return "Scissors"
        elif elf == "Paper":
            return "Rock"
        else:
            return "Paper"



#Open file
file = open("test.txt", "r")
#Test input
# file = open("t.txt", "r")

score = 0
lines = file.readlines()

for line in lines :
    elf = elfDict[line[0]]
    condition = MyDict[line[2]]
    me = getResponse(elf, condition)
    score = score + rspVals[me] + rspwlt(elf, me)
print(score)