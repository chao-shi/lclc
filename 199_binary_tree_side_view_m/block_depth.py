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
        def recur(root, block_depth):
            if not root:
                return []
            ret = []
            if block_depth == 0:
                ret.append(root.val)
            right = recur(root.right, max(0, block_depth - 1))
            ret.extend(right)
            left = recur(root.left, block_depth + len(ret) - 1)
            ret.extend(left)
            return ret
        
        return recur(root, 0)