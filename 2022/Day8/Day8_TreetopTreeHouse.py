## --- Day 8: Treetop Tree House ---
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. The Elves explain that a previous expedition planted these trees as a reforestation effort. Now, they're curious if this would be a good location for a tree house.
#
# First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.
#
# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:
#
# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.
#
# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
#
# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:
#
# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.
#
# Consider your map; how many trees are visible from outside the grid?
# Your puzzle answer was 1647.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: they would like to be able to see a lot of trees.
#
# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)
#
# The Elves don't care about distant trees taller than those found by the rules above; the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.
#
# In the example above, consider the middle 5 in the second row:
#
# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is not blocked; it can see 1 tree (of height 3).
# Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
# Looking right, its view is not blocked; it can see 2 trees.
# Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).
#
# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:
#
# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
# Looking left, its view is not blocked; it can see 2 trees.
# Looking down, its view is also not blocked; it can see 1 tree.
# Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.
#
# Consider each tree on your map. What is the highest scenic score possible for any tree?
import numpy as np

#Function finds the index of the first element in the input list that is greater than val
def treescore(input,val):
    try:
        value= next((index for index, item in enumerate(input) if item > (val-1)),None)+1
    except:
        value=len(input)
    return value

#Read file and save all lines into array
with open('AdventofCode/2022/Day8/PuzzleInput.txt','r') as f:
    lines = f.readlines()
adjustedstrings = []
for l in lines:
    adjustedstrings.append(l.replace('\n',''))
treeheights=[]
treerow=[]
for l in adjustedstrings:
    for i in range(len(l)):
        treerow.append(int(l[i]))
    treeheights.append(treerow)
    treerow = []

#Transpose the matrix to make it easier to search up and down
arr1 =  np.array(treeheights)
treeheightsT = (arr1.transpose()).tolist()

#Create empty arrays
visibletrees=[]
visiblerow=[]
treescores=[]
rowscore=[]

#Loop through all trees in each row
for i in range(0,len(treeheights)):
    for j in range(0,len(l)):
        #extract current tree value
        tree=treeheights[i][j]

        #get an array of all trees left of the chosen tree
        lefttrees=treeheights[i][:j]
        #If tree is in the left most collumn, it has a score of 0 and it is always visible
        if lefttrees==[]:
            maxlefttree=-1
            Lscore=0
        #If it is somewhere in the matrix, check if it is bigger than all to the left.
        else:
            maxlefttree=max(lefttrees)
            #reverse array and check distance to first tree that is same size or bigger
            adjustedleft=lefttrees[::-1]
            Lscore=treescore(adjustedleft,tree)

        #get an array of all trees up from the chosen tree
        uptrees=treeheightsT[j][:i]
        #If tree is in the top row, it has a score of 0 and it is always visible
        if uptrees==[]:
            maxuptree= -1
            Uscore= 0
        #If it is somewhere in the matrix, check if it is bigger than all above
        else:
            maxuptree=max(uptrees)
            #reverse array and check distance to first tree that is same size or bigger
            adjustedup=uptrees[::-1]
            Uscore=treescore(adjustedup,tree)

        #get an array of all trees down from the chosen tree
        downtree=treeheightsT[j][(i+1):]
        #If tree is in the bottom row, it has a score of 0 and it is always visible
        if downtree==[]:
            maxdowntree=-1
            Dscore=0
        #If it is somewhere in the matrix, check if it is bigger than all above
        else:
            maxdowntree=max(downtree)
            #check distance to first tree that is same size or bigger
            Dscore=treescore(downtree,tree)

        #get an array of all trees to the right from the chosen tree
        righttrees=treeheights[i][(j+1):]
        #If tree is in the right most column, it has a score of 0 and it is always visible
        if righttrees==[]:
            maxrighttree=-1
            Rscore=0
        #If it is somewhere in the matrix, check if it is bigger than all above
        else:
            maxrighttree=max(righttrees)
            #check distance to first tree that is same size or bigger
            Rscore=treescore(righttrees,tree)

        #Is the tree visible?
        if(tree>maxlefttree or tree>maxuptree or tree>maxdowntree or tree>maxrighttree):
            visiblerow.append(1)
        else:
            visiblerow.append(0)

        #Calculate tree score based off all directions and add to the row array
        rowscore.append(Lscore*Rscore*Dscore*Uscore)

    #add row arrays to overall matrix's and clear temp row arrays
    visibletrees.append(visiblerow)
    visiblerow=[]
    treescores.append(rowscore)
    rowscore=[]

#calculate number of visual tree for Part A
val=0
for l in visibletrees:
    val+=sum(l)

print('Part 1: '+ str(val))

#Find tree with the highest score for Part B
maxrows=[]
for r in treescores:
    maxrows.append(max(r))

print('Part 2: '+str(max(maxrows)))
