# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def pad(s, n):
            padding = (n - len(s)) / 2
            return [""] * padding  + s + [""] * padding

        def recur(root):
            if not root:
                return [], 0, 0
            left_matrix, ml, nl = recur(root.left)
            right_matrix, mr, nr = recur(root.right)
            
            width = max(nl, nr)
            matrix = [pad([str(root.val)], 2 * width + 1)]
            for i in range(max(ml, mr)):
                ls = left_matrix[i] if i < len(left_matrix) else [""]
                rs = right_matrix[i] if i < len(right_matrix) else [""]
                row = pad(ls, width) + [""] + pad(rs, width)
                matrix.append(row)
            return matrix, len(matrix), len(matrix[0])
        
        return recur(root)[0]
        
        

# Wrong implementation of using pading
# +5+
# 4+6
# needs to expand to
# +++++5+++++
# ++4+++++6++
# Logic not so easy  
