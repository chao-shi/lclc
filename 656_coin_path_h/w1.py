class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        # (a, b) where a is the min coins needed to reach here and b is last stop
        # a = None means impossible to reach here
        # b = None means first element or a is None
        opt = [(A[0], None)]
        
        for i in range(1, len(A)):
            if A[i] == -1:
                opt.append((None, None))
            else:
                coin, last_step = None, None
                for j in range(max(0, i - B), i):
                    # if opt[j][0] != None and (coin == None or opt[j][0] + A[i] < coin):
                    if opt[j][0] != None and (coin == None or opt[j][0] + A[i] <= coin):

                        coin = opt[j][0] + A[i]
                        last_step = j
                opt.append((coin, last_step))

        if opt[-1][0] == None:
            return []

        steps = []
        i = len(A) - 1
        while i != None:
            steps.append(i)
            i = opt[i][1]
        return map(lambda x:x + 1, steps[::-1])

# The difficult part is how to get lexico order right in case of coin tie.
# Line 19 cannot do case 
# [0,0,0,0,0,0] 3 right. It prefers to take a shorter path of 1, 3, 6 instead of 1,2,3,4,5,6

# Line 20 cannot do this right, it will take the wrong of line 2
# [1, ..... 2 ....  ......5]
# [1, ...........2, ......5]

# To solve it foundamentally, we need to iterate backwards.