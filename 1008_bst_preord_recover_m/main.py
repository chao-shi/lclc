# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        left_node_stack = [root]

        for i in range(1, len(preorder)):
            v = preorder[i]
            node = TreeNode(v)
            if left_node_stack and left_node_stack[-1].val > v:
                left_node_stack[-1].left = node
                left_node_stack.append(node)
            else:
                right_parent_cand = None
                while left_node_stack and left_node_stack[-1].val < v:
                    right_parent_cand = left_node_stack.pop()
                # Now the one on top can host node on the left, we are still
                # in left tree
                right_parent_cand.right = node
                left_node_stack.append(node)
        return root
        