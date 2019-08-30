# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        hei_map = collections.defaultdict(int)
        def maxHeight(root):
            if not root:
                height = 0
            else:
                height = 1 + max(maxHeight(root.left), maxHeight(root.right))
            hei_map[root] = height
            return height
            
        maxHeight(root)
        
        def findAncestor(root):
            if not root:
                return None
            else:
                h1, h2 = hei_map[root.left], hei_map[root.right]
                if h1 == h2:
                    return root
                elif h1 > h2:
                    return findAncestor(root.left)
                else:
                    return findAncestor(root.right)
                
        return findAncestor(root)
    
# How to improve, this approach is good because findAncestor may not need to call recursion, it can early break
# One function recursion, maybe we need to have the parent overwrite the children