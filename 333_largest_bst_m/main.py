# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def smaller(a, b):
    if a == None:
        return b
    elif b == None:
        return a
    return min(a, b)

def bigger(a, b):
    if a == None:
        return b
    elif b == None:
        return a
    return max(a, b)

class Solution(object):

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # The third return value is None if tree is invalid
        self.max_v = 0
        def recur(root):
            if not root:
                return None, None, 0
            
            left_min, left_max, left_c = recur(root.left)
            right_min, right_max, right_c = recur(root.right)

            if left_c != None and (left_max == None or left_max < root.val) and \
                right_c != None and (right_min == None or root.val < right_min):
                    self.max_v = max(self.max_v, 1 + left_c + right_c)
                    return smaller(root.val, left_min), bigger(root.val, right_max), 1 + left_c + right_c
            else:
                return None, None, None
        
        recur(root)
        return self.max_v