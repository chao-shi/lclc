class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = []
        s_i = 0
        for idx, src, tar in sorted(zip(indexes, sources, targets)):
            res.append(S[s_i:idx])
            if src == S[idx:idx+len(src)]:
                res.append(tar)
            else:
                # no overlapping guranteed
                res.append(S[idx:idx+len(src)])
            s_i = idx + len(src)
        res.append(S[s_i:])
        return "".join(res)
        