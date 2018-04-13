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
        if not root:
            return []
        
        res = []
        if root.left:
            res.extend(map(lambda x:str(root.val) + "->" + x, self.binaryTreePaths(root.left)))
        if root.right:
            res.extend(map(lambda x:str(root.val) + "->" + x, self.binaryTreePaths(root.right)))
        return res if res else [str(root.val)]