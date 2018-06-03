# First needs to sort the array for example [5,2,6,1] 
# becomes [1, 2, 5, 6] and use the index to represent each number

# Seg Tree Node will store the starting and ending index
# The root will be [0, 4, 4], meaning that from between [n[0] and n[3]], there are 4 elements

# This solves the segment tree problem such that the number value is unbounded.

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/3-ways-(Segment-Tree-Binary-Indexed-Tree-Binary-Search-Tree)-clean-python-code