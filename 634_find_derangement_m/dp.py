# C(N) = (N-1) * (C(N-1) + C(N-2))
# In order to generate the derangements of this array, assume that firstly, 
# we move the number 1 from its original position and place at the place of the number i. But, now, this ith 
# position can be chosen in n-1 ways. Now, for placing the number i we have got two options: 
# 1. Swap 1st and ith number, this is reduced to sub problem of N-2
# 2. Put 1 into ith index, move ith number to index other than 1. This reduce to N-1 problem. Why
#    Now only number 1 is placed. The other N-1 numbers are subject to the same condition except number i cannot be put on index 1