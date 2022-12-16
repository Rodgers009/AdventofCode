import numpy as np

#Return the number of unique entries in a list
def uniquevals(list):
    array = np.array(list)
    unique = np.unique(array)
    return len(unique)

#Read file and save all lines into array
with open('AdventofCode/2022/Day9/PuzzleInput.txt','r') as f:
    lines = f.readlines()
adjustedstrings = []
for l in lines:
    adjustedstrings.append(l.replace('\n',''))

#Create initial Locations of the Head and Tail. Start at a (0,0) coordinate
HLocation=[0,0]
LLocation=[0,0]
allTailLocations=[]

for l in adjustedstrings:
    if l[0]=='L':
        #Extract number of steps in direction noted above
        for i in range(int(l[1:])):
            # If the Head is already diagonal to the Tail in the direction of travel,
            # the tail needs to move to the same Y coordinate
            if((HLocation[0]<LLocation[0]) and (HLocation[1] != LLocation[1])):
                LLocation[1]=HLocation[1]
            # Move X coordinate one to left
            HLocation[0]+=-1
            # If the Tail moves 2 steps away from Head, Tail travels with Head
            if(abs(LLocation[0]-HLocation[0])>1):
                LLocation[0]+=-1
            # Add new X and Y coordinate of Tail to allTailLocations list
            allTailLocations.append([LLocation[0],LLocation[1]])
    if l[0]=='R':
        #Extract number of steps in direction noted above
        for i in range(int(l[1:])):
            # If the Head is already diagonal to the Tail in the direction of travel,
            # the tail needs to move to the same Y coordinate
            if((HLocation[0]>LLocation[0]) and (HLocation[1] != LLocation[1])):
                LLocation[1]=HLocation[1]
            # Move X coordinate of Head one to right
            HLocation[0]+=1
            # If the Tail moves 2 steps away from Head, Tail travels with Head
            if(abs(LLocation[0]-HLocation[0])>1):
                LLocation[0]+=1
            # Add new X and Y coordinate of Tail to allTailLocations list
            allTailLocations.append([LLocation[0],LLocation[1]])
    if l[0]=='U':
        #Extract number of steps in direction noted above
        for i in range(int(l[1:])):
            # If the Head is already diagonal to the Tail in the direction of travel,
            # the tail needs to move to the same Y coordinate
            if((HLocation[1]>LLocation[1]) and (HLocation[0] != LLocation[0])):
                LLocation[0]=HLocation[0]
            # Move X coordinate of Head one to right
            HLocation[1]+=1
            # If the Tail moves 2 steps away from Head, Tail travels with Head
            if(abs(LLocation[1]-HLocation[1])>1):
                LLocation[1]+=1
            # Add new X and Y coordinate of Tail to allTailLocations list
            allTailLocations.append([LLocation[0],LLocation[1]])
    if l[0]=='D':
        #Extract number of steps in direction noted above
        for i in range(int(l[1:])):
            # If the Head is already diagonal to the Tail in the direction of travel,
            # the tail needs to move to the same Y coordinate
            if((HLocation[1]<LLocation[1]) and (HLocation[0] != LLocation[0])):
                LLocation[0]=HLocation[0]
            # Move X coordinate of Head one to right
            HLocation[1]+=-1
            # If the Tail moves 2 steps away from Head, Tail travels with Head
            if(abs(LLocation[1]-HLocation[1])>1):
                LLocation[1]+=-1
            # Add new X and Y coordinate of Tail to allTailLocations list
            allTailLocations.append([LLocation[0],LLocation[1]])

#Append all values into a list of strings so the uniquevals function is able to differentiate between [0,1] and [1,0]
strvals=[]
for l in allTailLocations:
    strvals.append(str(l[0])+'_'+str(l[1]))

print(strvals)
print(uniquevals(strvals))
