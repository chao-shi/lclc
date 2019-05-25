# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if s == "":
            return None
        
        tokens = filter(lambda x:x, re.split("([\(|\)])", s))
        stack = []

        for t in tokens:
            if t == "(":
                continue
            elif t == ")":
                child = stack.pop()
                if stack[-1].left:
                    stack[-1].right = child
                else:
                    stack[-1].left = child
            else:
                root = TreeNode(int(t))
                stack.append(root)
        return stack[-1]