class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        visited = set()
        neighbor = {}
        for e in edges:
            neighbor.setdefault(e[0], set()).add(e[1])
            neighbor.setdefault(e[1], set()).add(e[0])

        self.max_path = 0
        self.cands = []

        # update global using longest path (any to any) in the current subtree
        # Locally return longest root path
        def recur(root):
            visited.add(root)
            root_paths = [[]]
            for n in neighbor.get(root, set()):
                if n not in visited:
                    root_paths.append(recur(n))
            
            # Not very good way to handle
            if len(root_paths) < 2:
                top_2_paths = [[], []]
            else:
                top_2_paths = sorted(root_paths, key=lambda p:-len(p))[:2]
            full_path = top_2_paths[0][::-1] + [root] + top_2_paths[1]

            # Longest paths must cross at the center, so simply overwrite
            length = len(full_path)
            if self.max_path <= length:
                self.cands = [full_path[length/2]] if length % 2 == 1 else full_path[length/2-1:length/2+1]
                self.max_path = len(full_path)
            
            return [root] + top_2_paths[0]

        if n == 0:
            return []
        recur(0)
        return self.cands
        