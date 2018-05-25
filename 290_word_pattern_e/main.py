class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern) != len(str):
            return False
        
        dict = {}
        rdict = {}
        for i, p in enumerate(pattern):
            if p in dict and dict[p] != str[i]:
                return False
            dict[p] = str[i]
            
            if str[i] in rdict and rdict[str[i]] != p:
                return False
            rdict[str[i]] = p
        return True
            