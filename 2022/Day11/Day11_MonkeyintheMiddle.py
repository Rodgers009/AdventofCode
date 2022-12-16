import math

#Read file and save all lines into array
with open('AdventofCode/2022/Day11/PuzzleInput.txt','r') as f:
    lines = f.readlines()
adjustedstrings = []
for l in lines:
    adjustedstrings.append(l.replace('\n',''))

original=[]

for idx, l in enumerate(adjustedstrings):
    cycle=(idx+1)%7
    #First Line defines monkey number. Doesn't matter
    if cycle==1:
        continue
    #Second Line defines monkey starting items seperated by ,
    elif cycle==2:
        vals=l[17:]
        items=vals.split(", ")
        items=[int(i) for i in items]
    #Third Line defines operation done on items
    elif cycle==3:
        op=l[23:]
        operators=[op[0],op[2:]]
    #Fourth Line defines divisible test
    elif cycle==4:
        divisible=int(l[21:])
    #Fifth line is the monkey to be thrown to if true
    elif cycle==5:
        truemonkey=int(l[29:])
    #Sixth line is the monkey to be thrown to if false and add all data to list
    elif cycle==6:
        falsemonkey=int(l[30:])
        original.append([items,operators,divisible,[truemonkey,falsemonkey]])
    #Seventh line is the end of monkey definition so add all data to list
    elif cycle==0:
        continue

partA=original
#Create an empty array of total iterations each monkey has run through
totals=[]
for w in range(len(partA)):
    totals.append(0)

#calculate divisor to be used to perform the extremely large arithmetic for part B
divisor=1
for i in original:
    divisor*=i[2]


#iterate through all monkeys
for j in range (0,10000):
    for jdx, monkey in enumerate(partA):
        #iterate through all items monkey has possestion of
        for idx, item in enumerate(monkey[0]):
            #perform operation on the item
            if monkey[1][0]=='*':
                if monkey[1][1] != 'old':
                    val = item*int(monkey[1][1])
                else:
                    val = item*item
            if monkey[1][0]=='+':
                if monkey[1][1] != 'old':
                    val = item+int(monkey[1][1])
                else:
                    val = item+item

            #Part A: Calculate the bored value
            #boredval = math.floor(val/3)


            #Part B: need to find a way to handle extremely large numbers.
            # Might be possible to find the modulus of the value by the product of all
            # divsors in the puzzle input. This would allow us to continue passing a smaller
            # value around that the CPU/RAM can handle but still hold the 'resolution' of the
            # originl problem? EDIT: Holy shitballs this worked...
            boredval = val%(divisor)


            #Determine which monkey to throw to
            if (boredval % monkey[2]) == 0:
                destmonkey=monkey[3][0]
            else:
                destmonkey=monkey[3][1]
            #Moved the scaled value to the destination monkey
            partA[destmonkey][0].append(boredval)
            #Store the number of items iterated through for this monkey. Used below
            pops=idx
            #iterate count for individual monkey counts
            totals[jdx]+=1
        #remove all values iterrated through in the above scan of Monkeys inventory
        for i in range(pops,-1,-1):
            try:
                removedel=monkey[0].pop(i)
            except:
                continue
        #reset number of items held by monkey
        pops=0
#Order totals from largest to smallest
totals.sort(reverse=True)
print("Part A/B: "+ str(totals[0]*totals[1]))
