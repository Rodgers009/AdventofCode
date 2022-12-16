#Read file and save all lines into array
with open('AdventofCode/2021/Day1/PuzzleInput.txt','r') as f:
    lines = f.readlines()
adjustedstrings = []
for l in lines:
    adjustedstrings.append(int(l.replace('\n','')))

increases=0
decreases=0

for idx in range(1,len(adjustedstrings)):
    if adjustedstrings[idx]>adjustedstrings[idx-1]:
        increases+=1
    else:
        decreases+=1

slidingwindow=[]
for idx in range(2,len(adjustedstrings)):
    slidingwindow.append(adjustedstrings[idx]+adjustedstrings[idx-1]+adjustedstrings[idx-2])

increases2=0
decreases2=0
for idx in range(1,len(slidingwindow)):
    if slidingwindow[idx]>slidingwindow[idx-1]:
        increases2+=1
    else:
        decreases2+=1

print("Part A: "+str(increases))
print("Part B: "+str(increases2))
