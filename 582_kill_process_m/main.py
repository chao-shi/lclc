class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        child_map = collections.defaultdict(set)
        for i, p in enumerate(pid):
            child_map[ppid[i]].add(p)
        
        res = []
        def kill_recur(p):
            res.append(p)
            for ch in child_map[p]:
                kill_recur(ch)
                
        kill_recur(kill)
        return res