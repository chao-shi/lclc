# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def recur(root, path, psum):
            if root == None:
                pass
            elif root.left == None and root.right == None:
                if psum + root.val == sum:
                    res.append(map(lambda x: x.val, path) + [root.val])
            else:
                path.append(root)
                recur(root.left, path, psum + root.val)
                recur(root.right, path, psum + root.val)
                path.pop(-1)
        
        recur(root, [], 0)
        return res

# same logic structure as 112, block 17 and blcok 19 are important