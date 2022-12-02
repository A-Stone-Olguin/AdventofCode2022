
elfDict = {"A" : "Rock",
           "B" : "Paper",
           "C" : "Scissors"}

MyDict  = {"X" : "Rock",
           "Y" : "Paper",
           "Z" : "Scissors"}

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

#Open file
file = open("test.txt", "r")
#Test input
# file = open("t.txt", "r")

score = 0
lines = file.readlines()

for line in lines :
    elf = elfDict[line[0]]
    me = MyDict[line[2]]
    score = score + rspVals[me] + rspwlt(elf, me)
print(score)
