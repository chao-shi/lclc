class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def map_base(str):
            res = ["a"]
            for i in range(1, len(str)):
                chr_ord = ord('a') + ord(str[i]) - ord(str[0])
                if chr_ord < ord('a'):
                    chr_ord += 26
                res.append(chr(chr_ord))
            return "".join(res)
        
        map = {}
        for s in strings:
            base = map_base(s)
            map.setdefault(base, []).append(s)
        
        return [map[base] for base in map]

# How to handle case of ["ba", "az"]
# Add the difference as usual, if out of range, below a or above z, adjust by +/- 26