# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        def pre_order(root, path):
            if not root:
                return
            
            path.append(root.val)
            if not root.left and not root.right:
                self.res.append("->".join(map(str, path)))
            
            pre_order(root.left, path)
            pre_order(root.right, path)
            path.pop()
            
        pre_order(root, [])
        return self.res

# This approach same complexity as
# divide/conquer/combine