class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        def merge(intvs):
            if not intvs:
                return []

            intvs = sorted(intvs)
            merged = [intvs[0]]
            for i in range(1, len(intvs)):
                if intvs[i][0] > merged[-1][1]:
                    merged.append(intvs[i])
                else:
                    merged[-1] = (merged[-1][0], max(intvs[i][1], merged[-1][1]))
            return merged

        intvs = []
        for w in dict:
            # re not working here, it only return non-overlapping
            # intvs.extend([(i.start(), i.end()) for i in re.finditer(w, s)])
            intvs.extend([(i, i + len(w)) for i in range(len(s)) if s[i:i+len(w)] == w])
        merged = merge(intvs)
        
        last_idx = 0
        res = []
        for intv in merged:
            res.append(s[last_idx:intv[0]])
            res.append("<b>{}</b>".format(s[intv[0]:intv[1]]))
            last_idx = intv[1]
        res.append(s[last_idx:])
        return "".join(res)
            
