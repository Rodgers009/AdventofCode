#Read file and save all lines into array
with open('AdventofCode/2022/Day10/PuzzleInput.txt','r') as f:
    lines = f.readlines()
adjustedstrings = []
for l in lines:
    adjustedstrings.append(l.replace('\n',''))

ValX=1
cycle=0
index=[]
GPURender=''

def incrementclock():
    global ValX,cycle,index,GPURender

    #PartA:
    #cycle+=1
    shiftedval=cycle%40
    if cycle==20 or (cycle - 20) %40 == 0:
        index.append(cycle*ValX)

    if (abs(shiftedval-ValX)<2):
        GPURender+='#'
    else:
        GPURender+='.'
    #PartB:
    cycle+=1

for idx, l in enumerate(adjustedstrings):
    if l[:4]=='addx':
        incrementclock()
        incrementclock()
        ValX+=int(l[4:])
    else:
        incrementclock()

#print('Part A: '+str(sum(index)))

print('Part B: ')
for i in range(0,len(GPURender),40):
    print(GPURender[i:i+40])
