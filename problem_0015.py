# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?



import math
#Lattice  of nxn is defined from (0,0) -> (n,n); we need lattice paths which equal (2n)Cn

answer = math.comb(40,20)
print(answer)

#137846528820