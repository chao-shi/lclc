# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        level = [root]
        reverse = False
        while level:
            if reverse:
                res.append(map(lambda x:x.val, level[::-1]))
            else:
                res.append(map(lambda x:x.val, level))
            level = [child for p in level for child in [p.left, p.right] if child]
            reverse = not reverse
        return res