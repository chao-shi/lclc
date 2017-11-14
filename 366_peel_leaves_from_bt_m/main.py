# 32ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        else:
            ll = self.findLeaves(root.left)
            rl = self.findLeaves(root.right)
            length = max(len(ll), len(rl))
            for i in range(length):
                if i >= len(ll):
                    ll.append([])
                if i < len(rl):
                    ll[i].extend(rl[i])
            ll.append([root.val])
            return ll