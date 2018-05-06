class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def permutation(char_cnt, prefix, res):
            if len(char_cnt) == 0:
                res.append(prefix)
            for ch in char_cnt:
                char_cnt[ch] -= 1
                if char_cnt[ch] == 0:
                    del char_cnt[ch]
                permutation(char_cnt, prefix + ch, res)
                char_cnt[ch] = char_cnt.get(ch, 0) + 1
        
        char_cnt = {}
        for ch in s:
            char_cnt[ch] = char_cnt.get(ch, 0) + 1
        
        pivot = ""
        for ch in char_cnt.keys():
            if char_cnt[ch] % 2 == 1:
                pivot += ch
            char_cnt[ch] /= 2
            
            # Don't forget here
            if char_cnt[ch] == 0:
                del char_cnt[ch]
        
        if len(pivot) > 1:
            return []
        
        res = []
        permutation(char_cnt, "", res)
        return map(lambda s:s + pivot + s[::-1], res)

# Line 28, because of the ending condition of line 8