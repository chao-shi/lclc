class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        cnt_map = collections.defaultdict(int)
        for ch in S:
            cnt_map[ch] += 1
            
        if any(cnt_map[ch] > (len(S) + 1)/ 2 for ch in cnt_map):
            return ""
        
        res = []

        for _ in range(len(S)):
            max_ch = None
            for ch in cnt_map:
                if (not res or ch != res[-1]) and (max_ch == None or cnt_map[ch] > cnt_map[max_ch]):
                    max_ch = ch
            if max_ch == None:
                return ""
            
            cnt_map[max_ch] -= 1
            res.append(max_ch)
        
        return "".join(res)
                