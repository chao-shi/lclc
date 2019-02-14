# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        while len(q) > 0:
            level_end = None
            for i in range(len(q)):
                level_end = q.popleft()
                if level_end.left:
                    q.append(level_end.left)
                if level_end.right:
                    q.append(level_end.right)
            res.append(level_end.val)
        return res