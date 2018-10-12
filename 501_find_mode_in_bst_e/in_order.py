# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.max_cnt = 0
        self.res = []

        def in_order(root, last, cnt):
            if not root:
                return last, cnt
            last, cnt = in_order(root.left, last, cnt)
            
            if root.val == last:
                cnt += 1
            else:
                last = root.val
                cnt = 1
            
            if cnt > self.max_cnt:
                self.max_cnt = cnt
                self.res = [root.val]
            elif cnt == self.max_cnt:
                self.res.append(root.val)
            
            last, cnt = in_order(root.right, last, cnt)
            return last, cnt
            
        
        in_order(root, None, 0)
        return self.res
        