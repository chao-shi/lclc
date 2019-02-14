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
        result = []
        
        def recur(root, depth):
            if not root:
                return
            if depth == len(result):
                result.append(root.val)
            else:
                result[depth] = root.val

            recur(root.left, depth + 1)
            recur(root.right, depth + 1)
        
        recur(root, 0)
        return result

# This one left first, then right