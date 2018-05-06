class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def first_diff_index(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    return i
            return min(len(w1), len(w2))

        def topo_sort(root, edges, res, visited):
            if root in visited:
                return visited[root] == 1
            visited[root] = 0
            for next in edges.get(root, []):
                if not topo_sort(next, edges, res, visited):
                    return False
            visited[root] = 1
            res.append(root)
            return True

        # Process edges
        edges = {}
        chars = set("".join(words))
        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            idx = first_diff_index(w1, w2)
            if idx < len(w1) and idx < len(w2):
                # edge (u, v) such that u is after v
                edges.setdefault(w2[idx], set()).add(w1[idx])
        
        res = []
        visited = {}
        for ch in chars:
            if not topo_sort(ch, edges, res, visited):
                return ""
        return "".join(res)
# Test case: ["wa", "wb"], where is w is unknown
# Must reuse the same visited map in lin 35