# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Forward direction, then stack end at the right
        if not root:
            return []
        right_stack_end = True
        stack = [root]
        res = []
        while stack:
            res.append([])
            new_stack = []
            while stack:
                top = stack.pop()
                res[-1].append(top.val)
                nexts = [top.left, top.right] if right_stack_end else[top.right, top.left]
                for n in nexts:
                    if n:
                        new_stack.append(n)
            stack = new_stack
            right_stack_end = not right_stack_end
        return res
