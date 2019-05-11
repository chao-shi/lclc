from collections import Counter
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def recur(s):
            cnt = Counter(s)
            invalid = set([ch for ch in cnt if cnt.get(ch) < k])
            if not invalid:
                return len(s)
            ret = 0
            splits = [-1] + [i for i, ch in enumerate(s) if ch in invalid] + [len(s)]
            for i in range(len(splits) - 1):
                ret = max(ret, recur(s[splits[i] + 1 : splits[i+1]]))
            return ret
        
        return recur(s)

# Divide and conquer