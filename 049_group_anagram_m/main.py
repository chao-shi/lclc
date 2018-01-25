class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def key(s):
            counter = collections.Counter(s)
            tuples = sorted([(key, str(counter.get(key))) for key in counter])
            # how to easily do flat map
            return "".join([e for tp in tuples for e in tp])
        
        d = {}
        for s in strs:
            k = key(s)
            if k not in d:
                d[k] = []
            d[k].append(s)
        
        return [d[k] for k in d]

# Slower than sorting as key in OJ. But this is O(N * K) where K is average length of string