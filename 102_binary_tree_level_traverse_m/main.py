# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        level = [root]
        while level:
            res.append(map(lambda x:x.val, level))
            level = [child for p in level for child in [p.left, p.right] if child]
        return res