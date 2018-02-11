# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        hm = {}
        def clone(node):
            if node in hm:
                return hm[node]
            newnode = UndirectedGraphNode(node.label)
            hm[node] = newnode
            newnode.neighbors = [clone(child) for child in node.neighbors]
            return newnode
        
        if not node:
            return None
        return clone(node)
    
# Line 16 location, keep in map before calling children