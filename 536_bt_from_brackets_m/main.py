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
        tokens = filter(lambda x:x, re.split("([\(|\)])", s))
        tokens = ["("] + tokens + [")"]

        def recur(i):
            if i > len(tokens) or tokens[i] !='(':
                return None, i
            elif tokens[i+1] == ')':
                return None, i+2
            else:
                rootval = int(tokens[i+1])
                root = TreeNode(rootval)
                left, i = recur(i+2)
                right, i = recur(i)
                root.left, root.right = left, right
                # skip ")"
                return root, i + 1
        
        return recur(0)[0]