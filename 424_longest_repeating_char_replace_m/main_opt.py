class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Find the longest substring with 
        # sum(char except most frequency) <= k
        i = 0
        bag = {}
        max_v = 0
        max_f = 0
        for j, ch in enumerate(s):
            bag[ch] = bag.get(ch, 0) + 1
            # j won't forward only if bag[ch] is now the unique biggest
            max_f = max(max_f, bag[ch])
            while j - i + 1 - max_f > k:
                bag[s[i]] -= 1
                i += 1
            max_v = max(max_v, j - i + 1)
        return max_v

# A simple follow up to to do alphabetic scan in valid_bag
# Keep the current most frequent
# Why this works?
# Even though we never update max_f in block 18
# 
# The nature of the question is to find max_f
# we have the option of put a window around max_f elements,
# If it cannot go any further up, we keep the window size fixed