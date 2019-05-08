class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # Stack to hold the temporary result of DDDDD
        stack = []
        n = len(s) + 1
        ans = []
        for i in range(1, n):
            if s[i-1] == "I":
                ans.append(i)
                ans.extend(stack[::-1])
                stack = []
            else:
                stack.append(i)
        ans.append(n)
        ans.extend(stack[::-1])
        return ans

# IIII
# Insert 1, check first I, wait next element to be greater
# 