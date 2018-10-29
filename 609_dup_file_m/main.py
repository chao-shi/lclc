class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_map = collections.defaultdict(set)
        for p in paths:
            segs = p.split()
            p_dir = segs[0]
            for i in range(1, len(segs)):
                sp = segs[i].find("(")
                file_name = segs[i][:sp]
                content = segs[i][sp+1:len(segs[i]) - 1]
                content_map[content].add("{}/{}".format(p_dir, file_name))
        
        res = []
        for c in content_map:
            if len(content_map[c]) > 1:
                res.append(list(content_map[c]))
        return res
                