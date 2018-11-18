class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        # (a, b) where a is the min coins needed if you are at i to reach the destination.
        # b is next stop
        # a = None means impossible to reach here
        # b = None means it is destination
        opt = [(None, None)] * (len(A) - 1) + [(A[-1] if A[-1] != -1 else None, None)]
        
        for i in range(len(A) - 2, -1, -1):
            if A[i] == -1:
                opt[i] = (None, None)
                continue
            
            coin, next_stop = None, None
            for j in range(i + 1, min(i+B+1, len(A))):
                # Don't replace if same, this guarantee the lexico order
                if opt[j][0] != None and (coin == None or opt[j][0] + A[i] < coin):
                    coin = opt[j][0] + A[i]
                    next_stop = j
            opt[i] = (coin, next_stop)

        if opt[0][0] == None:
            return []

        steps = []
        i = 0
        while i != None:
            steps.append(i)
            i = opt[i][1]
        return map(lambda x:x + 1, steps)
                
# Needs to GO backwards. Why, see w1.py