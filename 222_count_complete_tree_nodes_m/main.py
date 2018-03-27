# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root):
            cnt = 0
            while root:
                root, cnt = root.left, cnt + 1
            return cnt
        
        def recur(root):
            if not root:
                return 0
            h_left, h_mid = height(root), height(root.right) + 1
            if h_left == h_mid:
                return recur(root.right) + 2 ** (h_left - 1)
            else:
                return recur(root.left) + 2 ** (h_mid - 1)
        
        return recur(root)

# O(N) = O(N/2) + logN ** 2
# Final complexity is logN ** 2