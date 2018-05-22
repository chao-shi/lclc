# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cand1 = 0
        for i in range(1, n):
            if knows(cand1, i):
                cand1 = i
        cand2 = n - 1
        for i in range(n-2, -1, -1):
            if knows(cand2, i):
                cand2 = i

        if cand1 != cand2:
            return -1

        return cand1 if all(knows(i, cand1) for i in range(n) if i != cand1) else -1

# Tricky always to check if all knows cand