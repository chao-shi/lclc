class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        win = collections.defaultdict(int)
        counter = collections.Counter(p)
        i = 0
        res = []
        matched = 0
        for j in range(len(s)):
            win[s[j]] += 1
            if win[s[j]] <= counter.get(s[j]):
                matched += 1
                
            while j - i + 1 > len(p):
                win[s[i]] -= 1
                if win[s[i]] < counter.get(s[i]):
                    matched -= 1
                i += 1
            
            if matched == len(p) and j - i + 1 == len(p):
                res.append(i)
                
        return res
        
        