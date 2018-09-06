"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        ret = []
        
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                top = q.popleft()
                level.append(top.val)
                for ch in top.children:
                    q.append(ch)
            
            ret.append(level)
        return ret
# How to not store the depth and not use temporary storage