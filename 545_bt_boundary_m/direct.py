# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        if root.left == None:
            left_b = [root]
        else:
            left_b = []
            p = root
            while p:
                left_b.append(p)
                if p.left:
                    p = p.left
                else:
                    p = p.right
        
        if root.right == None:
            right_b = [root]
        else:
            right_b = []
            p = root
            while p:
                right_b.append(p)
                if p.right:
                    p = p.right
                else:
                    p = p.left
        
        
        def find_leaves(root, leaves):
            if root:
                if root.left == None and root.right == None:
                    leaves.append(root)
                if root.left:
                    find_leaves(root.left, leaves)
                if root.right:
                    find_leaves(root.right, leaves)
        
        leaves= []
        find_leaves(root, leaves)
        
        if left_b[-1] == leaves[0]:
            left_b.pop()
        if right_b[-1] == leaves[-1]:
            right_b.pop()
        
        ans = left_b + leaves + right_b[1:][::-1]
        return map(lambda x:x.val, ans)

# Pre-order solution is not so cool. Many state variables
# 