class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict = {}
        for w in words:
            mask = reduce(lambda x, y: x | y, [1 << (ord(ch) - ord('a')) for ch in w], 0)
            dict.setdefault(mask, len(w))
            dict[mask] = max(dict[mask], len(w))
            
        max_v = 0
        for m1 in dict:
            for m2 in dict:
                if m1 & m2 == 0:
                    max_v = max(max_v, dict[m1] * dict[m2])
        return max_v
                            
# Good usage of the reduce function
# Reduce takes reduce lambda function, list and initial value to handle the empty list case