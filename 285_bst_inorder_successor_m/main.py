# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        left_tree = []
        q = root
        while q != p:
            if q.val < p.val:
                q = q.right
            else:
                left_tree.append(q)
                q = q.left
        
        q = p.right
        if q:
            while q.left != None:
                q = q.left
            return q
        elif left_tree:
            return left_tree[-1]
        else:
            return None
                
        