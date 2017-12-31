class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # Even better, know the index iterating before
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j == len(strs[i]) or strs[i][j] != strs[0][j]:
                    return strs[0][:j]
        return strs[0]