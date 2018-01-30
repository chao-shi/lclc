# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [[root, 0]]
        res = []
        while stack:
            node, ic = stack[-1]
            if not node or ic == 3:
                stack.pop()
            else:
                stack[-1][1] += 1
                if ic == 0:
                    stack.append([node.left, 0])
                elif ic == 1:
                    res.append(node.val)
                else:
                    stack.append([node.right, 0])
        return res