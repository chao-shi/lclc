class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        root = 1
        neigh_map = collections.defaultdict(set)
        
        for e in edges:
            neigh_map[e[0]].add(e[1])
            neigh_map[e[1]].add(e[0])
                
        # Check if v is reachable from u
        def check_conn(u, v, curr, visited):
            if curr == v:
                return True
            else:
                for nei in neigh_map[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        if check_conn(u, v, nei, visited):
                            return True
                        visited.remove(nei)
                return False
            
        
        last_edge = None
        for u, v in edges:
            neigh_map[u].remove(v)
            neigh_map[v].remove(u)
            if check_conn(u, v, u, set()):
                last_edge = [u, v]
            neigh_map[u].add(v)
            neigh_map[v].add(u)
        return last_edge

# DFS check edge by edge, Remove that edge to see if u, v still interconnected.