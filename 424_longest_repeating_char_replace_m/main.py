class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def valid_bag(bag):
            vs = bag.values()
            return sum(vs) - max(vs) <= k

        # Find the longest substring with 
        # sum(char except most frequency) <= k
        i = 0
        bag = {}
        max_v = 0
        for j, ch in enumerate(s):
            bag[ch] = bag.get(ch, 0) + 1
            while not valid_bag(bag):
                bag[s[i]] -= 1
                i += 1
            max_v = max(max_v, j - i + 1)
        return max_v