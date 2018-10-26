# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def pre_order(node, res):
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                pre_order(node.left, res)
                pre_order(node.right, res)
            return res
            
        ps, pt = pre_order(s, []), pre_order(t, [])
        ps, pt = ",".join(ps), ",".join(pt)
        # return ps.find(pt) != -1
        idx = ps.find(pt)
        return idx != -1 and (idx == 0 or ps[idx-1] == ',')
    
# Careful of case [12] and [2]
# KMP for speedup substring matching