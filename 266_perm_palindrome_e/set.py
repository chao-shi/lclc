class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bag = set()
        for ch in s:
            if ch in bag:
                bag.remove(ch)
            else:
                bag.add(ch)
        return len(bag) <= 1

# Cleaner