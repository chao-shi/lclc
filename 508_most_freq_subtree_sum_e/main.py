# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.cnt = collections.defaultdict(int)

        def recur(root):
            if root == None:
                return 0
            sumv = root.val + recur(root.left) + recur(root.right)
            self.cnt[sumv] += 1
            return sumv
        
        if not root:
            return []
        recur(root)
        max_cnt = max(self.cnt.values())
        return [n for n in self.cnt if self.cnt[n] == max_cnt]