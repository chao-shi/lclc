class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # When calculating 1-N permutation with length N
        # The sub problem is with length N - 1
        
        # For sub problem, the optimal solution is to take 1 to N - 1
        # Replacing any number in [1, N-1] with N will only end up bigger lexi order
        
        # Now we need to fit N into the solution of sub problem
        
        n = len(s) + 1
        ans = [1]
        last_I = -1
        for i in range(2, n + 1):
            # check new relation, easier if it is I
            # Otherwise if it is D, 
            # Needs to search the last seen "I" 
            # Pattern will be IDDDD....D
            
            # The idea is the invert the section of DDD...DD
            if s[i-2] == 'I':
                last_I = i - 2
            ans.insert(last_I + 1, i)
        return ans
                
# Pretty fast but not O(N)
# Can be O(N) if we rewrite line 25 here by popping and pushing 
# The reason is because last_I is always moving right