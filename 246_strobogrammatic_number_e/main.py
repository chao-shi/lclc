class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mapping = {
            "6": "9",
            "9": "6",
            "0": "0",
            "1": "1",
            "8": "8"
        }
        
        i, j = 0, len(num) - 1
        while i <= j and mapping.get(num[i], None) == num[j]:
            i, j = i + 1, j - 1
        
        return i > j