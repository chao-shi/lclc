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
            # Return LCA, number of nodes matched with p, q
            if root == None:
                return None, 0

            left_lca, m1 = recur(root.left)
            if left_lca:
                return left_lca, m1

            right_lca, m2 = recur(root.right)
            if right_lca:
                return right_lca, m2

            m = m1 + m2
            if root in [p, q]:
                m += 1

            if m == 2:
                return root, m
            else:
                return None, m
        
        return recur(root)[0]

# Single return vs 3 return approach
# Single return: return lca, else return either p or q
# Easier to write
# Always need to traverse entire tree
# 
# Discard it now, too difficult to explain