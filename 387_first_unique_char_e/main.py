class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {}
        cands = []
        for i in range(len(s)):
            if s[i] not in cnt:
                cands.append(i)
            cnt[s[i]] = cnt.get(s[i], 0) + 1
        
        for cand in cands:
            if cnt[s[cand]] == 1:
                return cand
        return -1