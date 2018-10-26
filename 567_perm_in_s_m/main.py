class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        bag = collections.defaultdict(int)
        cnt = collections.Counter(s1)
        i = 0
        for j, ch in enumerate(s2):
            bag[ch] += 1
            while bag[ch] > cnt[ch]:
                bag[s2[i]] -= 1
                i += 1
            if j + 1 - i == len(s1):
                return True
        return False