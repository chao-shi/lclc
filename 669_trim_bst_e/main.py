# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # def merge_tree(r1, r2):
        #     if r2 == None:
        #         return r1
        #     elif r2.left == None:
        #         r2.left = r1
        #         return r2
        #     else:
        #         p = r2
        #         while p.left and p.left.left != None:
        #             p = p.left
        #         nr = TreeNode(p.left.val)
        #         nr.left, nr.right = r1, r2
        #         p.left = None
        #         return nr
        
        def recur(root, L, R):
            if not root:
                return None
            lr = recur(root.left, L, R)
            rr = recur(root.right, L, R)
            if L <= root.val <= R:
                root.left, root.right = lr, rr
                return root
            # else:
                # return merge_tree(lr, rr)
            elif root.val > R:
                return lr
            else:
                return rr

        return recur(root, L, R)
        
# Description is little unclear. I first implemented the merge tree function if the root is out of range
# But when root is out of range, one side of tree will be complete empty, so only keep another side