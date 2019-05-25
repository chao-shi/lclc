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
        self.id = 1
        mt = {}
        def preprocess(root):
            if not root:
                return 0
            left_id = preprocess(root.left)
            right_id = preprocess(root.right)
            tp = (root.val, left_id, right_id)
            if tp not in mt:
                mt[tp] = self.id
                self.id += 1
            return mt[tp]

        root_id = preprocess(t)
        print root_id, mt
        
        def check(root):
            if root == None:
                my_root_id = 0
                return my_root_id == root_id, 0
            else:
                left_res, left_id = check(root.left)
                right_res, right_id = check(root.right)
                if left_res or right_res:
                    return True, None
                elif left_id != None and right_id != None:
                    tp = (root.val, left_id, right_id)
                    my_root_id = mt.get(tp)
                    return my_root_id == root_id, my_root_id
                else:
                    return False, None
        
        res, _ = check(s)
        return res