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
        self.id = 1
        self.id_map = {}
        self.id_cnt = collections.defaultdict(int)
        res = []
        
        def id_recur(root):
            if not root:
                return 0
            else:
                left_id = id_recur(root.left)
                right_id = id_recur(root.right)
                
                # Unique identification
                tp = (root.val, left_id, right_id)

                if tp in self.id_map:
                    idx = self.id_map[tp]
                else:
                    idx = self.id
                    self.id_map[tp] = idx
                    self.id += 1
                
                if self.id_cnt[idx] == 1:
                    res.append(root)
                self.id_cnt[idx] += 1
                return idx
            
        id_recur(root)
        return res
                
                    
            