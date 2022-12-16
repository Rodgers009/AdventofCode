#Read file and save all lines into array
with open('AdventofCode/2022/Day13/PuzzleInput.txt','r') as f:
    lines = f.readlines()
adjustedstrings = []
for l in lines:
    adjustedstrings.append(l.replace('\n',''))

print(adjustedstrings)
