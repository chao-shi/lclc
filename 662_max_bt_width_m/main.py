# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_idx = {}
        self.max_wid = 0
        def recur(node, idx):
            if not node:
                return
            depth = int(math.log(idx, 2))
            if depth not in min_idx:
                min_idx[depth] = idx
            self.max_wid = max(self.max_wid, idx - min_idx[depth] + 1)
            recur(node.left, idx * 2)
            recur(node.right, idx * 2 + 1)
        
        recur(root, 1)
        return self.max_wid
            