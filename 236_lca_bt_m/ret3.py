# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recur(root):
            if not root:
                return None, False, False
            l_lca, lp, lq = recur(root.left)
            if l_lca:
                return l_lca, True, True
            
            r_lca, rp, rq = recur(root.right)
            if r_lca:
                return r_lca, True, True
            
            pin, qin = (root == p) or lp or rp, (root == q) or lq or rq
            lca = root if pin and qin else None
            return lca, pin, qin
        
        return recur(root)[0]