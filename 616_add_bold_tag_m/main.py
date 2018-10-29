class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        intvs = []
        for w in dict:
            # re not working here, it only return non-overlapping
            # intvs.extend([(i.start(), i.end()) for i in re.finditer(w, s)])
            intvs.extend([(i, i + len(w)) for i in range(len(s)) if s[i:i+len(w)] == w])

        bolded = [False] * len(s)
        for intv in intvs:
            for i in range(intv[0], intv[1]):
                bolded[i] = True
                
        i = 0
        res = []
        while i < len(bolded):
            ii = i
            while i < len(bolded) and bolded[i] == bolded[ii]:
                i += 1
            template = "<b>{}</b>" if bolded[ii] else "{}"
            res.append(template.format(s[ii:i]))
        return "".join(res)
        