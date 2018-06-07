class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.edict = {}
        self.visited={}
        for e in edges:
            if not e[0] in self.edict:
                self.edict[e[0]] = []
            if not e[1] in self.edict:
                self.edict[e[1]] = []
            self.edict[e[0]].append(e)
            self.edict[e[1]].append([e[1], e[0]])
        
        cnt = 0
        for i in range(n):
            if not i in self.visited:
                self.dfs(i)
                cnt += 1

        return cnt
        
    def dfs(self, root):
        self.visited[root] = True
        if root in self.edict:
            for e in self.edict[root]:
                if not e[1] in self.visited:
                    self.dfs(e[1])