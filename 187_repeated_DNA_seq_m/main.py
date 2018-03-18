class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        code_map = {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3
        }
        
        j = 0
        hashcode = 0
        mod9 = 4 ** 9
        seen = {}
        ret = []

        for i, ch in enumerate(s):
            if i - j + 1 > 10:
                hashcode %= mod9
                j += 1
            hashcode *= 4
            hashcode += code_map[ch]
            
            # Ignore less than 10 digits
            # AAA, and AAAAAAA has same hashcode, careful
            if i - j + 1 != 10:
                continue

            if seen.get(hashcode, 0) == 1:
                ret.append(s[j:i+1])
            seen[hashcode] = seen.get(hashcode, 0) + 1
        
        return ret

# Rolling hash