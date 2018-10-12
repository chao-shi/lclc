# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        max_map = {}
        
        def recur(root, depth):
            if root:
                max_map[depth] = max(root.val, max_map.get(depth, None))
                recur(root.left, depth + 1)
                recur(root.right, depth + 1)
        
        recur(root, 0)
        return [max_map[k] for k in sorted(max_map.keys())]