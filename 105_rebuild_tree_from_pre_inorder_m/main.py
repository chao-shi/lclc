# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        idxmap = {num: i for i, num in enumerate(inorder)}
        def recur(s1, t1, s2, t2):
            if s1 == t1:
                return None
            idx = idxmap[preorder[s1]]
            root = TreeNode(preorder[s1])
            preorder_split = s1 + 1 + idx - s2
            root.left = recur(s1 + 1, preorder_split, s2, idx)
            root.right = recur(preorder_split, t1, idx + 1, t2)
            return root
        return recur(0, len(preorder), 0, len(inorder))