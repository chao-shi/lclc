class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def is_sub_seq(s1, s2):
            i = 0
            for j in range(len(s2)):
                if s2[j] == s1[i]:
                    i += 1
                    if i == len(s1):
                        return True
            return False
        
        ans = ""
        for w in d:
            if is_sub_seq(w, s):
                if len(w) > len(ans) or len(w) == len(ans) and w < ans:
                    ans = w
        return ans

# Don't sort, sorting is additional work