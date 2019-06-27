# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def recur(i1, j1, i2, j2):
            if i1 == j1:
                return None
            elif j1 == i1 + 1:
                return TreeNode(pre[i1])
            else:
                split = index_map[pre[i1 + 1]]
                left_len = split - i2 + 1
                left = recur(i1 + 1, left_len + i1 + 1, i2, i2 + left_len)
                right = recur(left_len + i1 + 1, j1, i2 + left_len, j2 - 1)
                root = TreeNode(pre[i1])
                root.left, root.right = left, right
                return root
            
        index_map = {num:i for i, num in enumerate(post)}
        return recur(0, len(pre), 0, len(post))