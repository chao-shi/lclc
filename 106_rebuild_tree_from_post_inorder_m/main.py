# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        idxmap = {num: i for i, num in enumerate(inorder)}
        def recur(s1, t1, s2, t2):
            if s1 == t1:
                return None
            idx = idxmap[postorder[t1-1]]
            root = TreeNode(postorder[t1-1])
            postorder_split = s1 + idx - s2
            root.left = recur(s1, postorder_split, s2, idx)
            root.right = recur(postorder_split, t1 - 1, idx + 1, t2)
            return root
        return recur(0, len(postorder), 0, len(inorder))
        