class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.cnt = 1

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        cnts = [0] * len(nums)
        root = TreeNode(nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            cnts[i] = self.helper(root, nums[i])
        return cnts
    
    # helper insert value and update the metadata along the route
    # return the count of smaller elements
    def helper(self, root, val):
        # Careful, always add cnt even though val is equal to root.val
        if root.val == val:
            ret_val = 0 if not root.left else root.left.cnt
        elif root.val < val:
            if not root.right:
                root.right = TreeNode(val)
                ret_val = root.cnt
            else:
                # Complex here
                ret_val = root.cnt - root.right.cnt + self.helper(root.right, val)
        else:
            if not root.left:
                root.left = TreeNode(val)
                ret_val = 0
            else:
                ret_val = self.helper(root.left, val)
        
        root.cnt += 1
        return ret_val