class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def is_sub_seq(s1, s2):
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            i = 0
            for j in range(len(s2)):
                if s2[j] == s1[i]:
                    i += 1
                    if i == len(s1):
                        return True
            return False
        
        cnt_map = collections.defaultdict(int)
        for s in strs:
            cnt_map[s] += 1
        
        # strs will be sorted by reverse length and no dup
        strs = sorted(cnt_map.keys(), key=lambda x:-len(x))
        
        for i, s in enumerate(strs):
            if cnt_map[s] == 1:
                if all(not is_sub_seq(strs[j], s) for j in range(i) if len(strs[j]) > len(strs[i])):
                    return len(s)
        return -1
                
        
# Sort strings by length reverse, the candidate will be unique string and it is not the sub seq of any string longer than it.