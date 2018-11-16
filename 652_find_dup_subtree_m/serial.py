# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ans = []
        hm = collections.defaultdict(int)

        def recur(root):
            if not root:
                serial = "#"
            else:
                serial = ",".join([str(root.val), recur(root.left), recur(root.right)])
            if root and hm[serial] == 1:
                ans.append(root)
            hm[serial] += 1
            return serial
        
        recur(root)
        return ans
                
            