# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def recur(root):
            if not root or not root.left:
                return root
            newroot = recur(root.left)
            # newroot will be 4 here
            # root.left will still be 2
            root.left.left, root.left.right = root.right, root
            root.left, root.right = None, None
            return newroot
        return recur(root)

# https://leetcode.com/problems/binary-tree-upside-down/discuss/49406/Java-recursive-(O(logn)-space)-and-iterative-solutions-(O(1)-space)-with-explanation-and-figure