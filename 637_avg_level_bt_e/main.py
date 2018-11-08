# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = collections.defaultdict(lambda : [0, 0])
        
        def recur(node, depth):
            if node:
                res[depth][0] += node.val
                res[depth][1] += 1
                recur(node.left, depth + 1)
                recur(node.right, depth + 1)
        
        recur(root, 0)
        ret = []
        for d in sorted(res.keys()):
            ret.append(float(res[d][0]) / float(res[d][1]))
        return ret
            