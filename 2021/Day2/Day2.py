#Read file and save all lines into array
with open('AdventofCode/2021/Day2/PuzzleInput.txt','r') as f:
    lines = f.readlines()
adjustedstrings = []
for l in lines:
    adjustedstrings.append(l.replace('\n',''))

splitstrings=[]
for l in adjustedstrings:
    splitstrings.append(l.split(' '))

location=[0,0,0]
for s in splitstrings:
    if s[0]=='forward':
        location[0]+=int(s[1])
        location[1]+=int(s[1])*location[2]
    elif s[0]=='up':
        #location[1]-=int(s[1])
        location[2]-=int(s[1])
    else:
        #location[1]+=int(s[1])
        location[2]+=int(s[1])

print("Part A/B: "+str(location[0]*location[1]))
