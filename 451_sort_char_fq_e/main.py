class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        clist = sorted([(counter.get(ch), ch) for ch in counter], reverse=True)
        res = ""
        for e in clist:
            res = res + e[1] * e[0]
        return res

# Some solution suggest bucket sorting. But the bucket is the frequency, and the range is 0 to len(s)
# 
# Though this saves sorting. This is a much worse solution. Scanning is O(N)
# 
# Sorting by frequencey is no bigger than O(KlogK) where K is the size of alphabets.
# 
# Sorting by frequency can be considered as constant instead.