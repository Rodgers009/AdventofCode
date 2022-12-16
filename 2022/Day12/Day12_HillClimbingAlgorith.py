from collections import deque

def CharacterPriority(char):
    ASCII = ord(char)
    if ASCII<91:
        priority = char
    else:
        priority = ASCII - 96
    return priority

#Read file and save all lines into array
with open('AdventofCode/2022/Day12/PuzzleInput.txt','r') as f:
    lines = f.readlines()
adjustedstrings = []
for l in lines:
    adjustedstrings.append(l.replace('\n',''))

#translate the letters to an integer representation of the map
intmap=[]
templist=[]
for l in adjustedstrings:
    for j in l:
        templist.append(CharacterPriority(j))
    intmap.append(templist)
    templist=[]

#Extract start and finish coordinates
startXY=[0,0]
EndXY=[0,0]
for idxY, i in enumerate(intmap):
    for idxX, j in enumerate(i):
        if j=='S':
            startXY=[idxX,idxY]
            intmap[idxY][idxX]=1
        elif j=='E':
            EndXY=[idxX,idxY]
            intmap[idxY][idxX]=27

#Navigate through matrix
location=startXY

#Create a queue that stores the possible movements as well as the distance from the original location.
# To begin with, it is starting at the 'S' coordinates with a distance of 0
Q=deque()

# partA: This dictates the starting point (0 distance) as 'S'
#Q.append(((startXY[1],startXY[0]),0))

#PART b: This dictates the starting point (0 distance) as any coordinate with a value of 1 (a)
for i in range(len(intmap)):
    for j in range(len(intmap[0])):
        if intmap[i][j] == 1:
            Q.append(((i,j),0))

#create a set of all the coordinates we have already travelled through
coordinates=set()
#As long as there are still possible alternatives to continue down, keep interating
while Q:
    #remove the leftmost step
    (y,x),d = Q.popleft()
    #If the coordinates of the step we're at have already been visited, skip it as we've already been there in less steps
    if (y,x) in coordinates:
        continue
    #Otherwise, add it to the set, along with its distance from the original location
    coordinates.add((y,x))
    #Check if we have reached the end coordinate
    if x==EndXY[0] and y== EndXY[1]:
        break
    #Check up, down, left and right locations
    for a,b in [(-1,0),(0,1),(1,0),(0,-1)]:
        newy=y+a
        newx=x+b
        #If the coordinate is within the map still and it is either 1 greater or less, add it to the queue and check its distance
        if((newy>=0)and(newy<len(intmap))and (newx>=0)and(newx<len(intmap[0])) and intmap[newy][newx]<=(1+intmap[y][x])):
            Q.append(((newy,newx),d+1))

# d will be written to last from the coordinate that causes the 'break' above. i.e. the end location
print('Part B: '+str(d))
