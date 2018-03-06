# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [[root, 0]]
        while stack:
            m = stack[-1]
            if not m[0] or m[1] == 3:
                stack.pop()
            else:
                if m[1] == 0:
                    res.append(m[0].val)
                elif m[1] == 1:
                    stack.append([m[0].left, 0])
                elif m[1] == 2:
                    stack.append([m[0].right, 0])
                m[1] += 1
        return res