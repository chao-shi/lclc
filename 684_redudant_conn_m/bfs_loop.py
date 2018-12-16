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
        
        q = collections.deque()
        q.append(root)
        ancestor_map = {root: None}

        node_i, node_j = None, None

        while q:
            top = q.popleft()
            for nei in neigh_map[top]:
                # Don't forget here
                if nei == ancestor_map[top]:
                    continue
                elif nei in ancestor_map:
                    node_i, node_j = nei, top
                    break
                else:
                    ancestor_map[nei] = top
                    q.append(nei)
            
        
        # At here two path between root to node_i
        path1 = []
        q = node_i
        while q != None:
            path1.append(q)
            q = ancestor_map[q]
        
        # path2 is root -> .... node_j, node_i
        path2 = []
        q = node_j
        while q:
            path2.append(q)
            q = ancestor_map[q]
        
        i, j = len(path1) - 1, len(path2) - 1
        while i >= 0 and j >= 0 and path1[i] == path2[j]:
            i, j = i - 1, j - 1
        path1, path2 = path1[:i+2], path2[:j+1][::-1]
        
        circle = path1 + path2
        circle_edges = set()
        for i in range(len(circle)):
            u, v = circle[i], circle[(i+1) % len(circle)]
            u, v = min(u, v), max(u, v)
            circle_edges.add((u, v))
    
        
        for e in edges[::-1]:
            if tuple(e) in circle_edges:
                return e
            