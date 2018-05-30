# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
        	return []
        level = [(root, 0)]
        colMap = {}
        while level:
            newlevel = []
            for tp in level:
                colMap.setdefault(tp[1], []).append(tp[0].val)

            	if tp[0].left != None:
            		newlevel.append((tp[0].left, tp[1] - 1))
            	if tp[0].right != None:
            		newlevel.append((tp[0].right, tp[1] + 1))
            level = newlevel

        sortedCols = sorted(colMap.keys())
        return [colMap[k] for k in sortedCols]
