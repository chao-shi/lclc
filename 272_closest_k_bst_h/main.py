# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # prev_stack stores all nodes needed iterating backwards
        # nodes such that current p is in its right tree
        prev_stack, next_stack = [], []
        
        def set_up_iterator():
            p = root
            while p:
                if p.val <= target:
                    prev_stack.append(p)
                    # if p.val == target:
                    #     break
                    p = p.right
                else:
                    next_stack.append(p)
                    p = p.left
        
        def move_previous():
            if prev_stack:
                p = prev_stack.pop().left
                while p:
                    prev_stack.append(p)
                    p = p.right
        
        def move_next():
            if next_stack:
                p = next_stack.pop().right
                while p:
                    next_stack.append(p)
                    p = p.left
        
        def peek_previous():
            return None if not prev_stack else prev_stack[-1].val
        
        def peek_next():
            return None if not next_stack else next_stack[-1].val

        set_up_iterator()
        res = []
        while len(res) < k:
            prev_val, next_val = peek_previous(), peek_next()
            if next_val == None:
                res.append(prev_val)
                move_previous()
            elif prev_val == None:
                res.append(next_val)
                move_next()
            elif abs(prev_val - target) <= abs(next_val - target):
                res.append(prev_val)
                move_previous()
            else:
                res.append(next_val)
                move_next()
        return res
    
# Early termination on line 25 is wrong. Next_stack may not finish the job yet
# K + Log(N)
# Brilliant solution