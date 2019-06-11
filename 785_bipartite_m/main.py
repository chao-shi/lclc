class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        # Can be a cycle in bipartite
        # DFS component by component
        # The starting point of a component can be any partite            
        def recur(n, col):
            if n in color_map:
                return color_map[n] == col
            color_map[n] = col
            for nei in graph[n]:
                if not recur(nei, 1 - col):
                    return False
            return True
            
        color_map = {}
        for n in range(len(graph)):
            if n not in color_map:
                if not recur(n, 0):
                    return False
        return True
        
# 1, 3
# 2, 3
# 2, 4

