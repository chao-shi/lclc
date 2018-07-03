class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        tokens = preorder.split(",")
        
        def recur(i):
            if i == len(tokens):
                return None
            elif tokens[i] == "#":
                return i + 1
            else:
                i = recur(i + 1)
                if i == None:
                    return None
                return recur(i)
        
        i = recur(0)
        return i == len(tokens)
    
# Handles "" well, "" is not a valid tree
# Don't return False, False == 0 is True