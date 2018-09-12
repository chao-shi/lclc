# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def delete(root, key):
            if not root:
                return None
            elif root.val < key:
                root.right = delete(root.right, key)
                return root
            elif root.val > key:
                root.left = delete(root.left, key)
                return root
            elif root.right == None:
                return root.left
            else:
                p = root.right
                while p.left != None:
                    p = p.left
                root.val = p.val
                root.right = delete(root.right, p.val)
                return root

        return delete(root, key)