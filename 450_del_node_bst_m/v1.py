# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def search(root, key):
            prev = None
            while root and root.val != key:
                prev = root
                if root.val < key:
                    root = root.right
                else:
                    root = root.left
            return prev, root
        
        # Return the new root
        def delete_node(root, del_node, prev):
            if not del_node.right:
                if prev and prev.right == del_node:
                    prev.right = del_node.left
                    return root
                elif prev and prev.left == del_node:
                    prev.left = del_node.left
                    return root
                else:
                    return root.left
            else:
                prev_p, p = None, del_node.right
                while p.left != None:
                    prev_p, p = p, p.left
                del_node.val = p.val
                # delete_node(root.right, p, prev_p)
                del_node.right = delete_node(del_node.right, p, prev_p)
                return root
        
        prev, node = search(root, key)
        if node:
            return delete_node(root, node, prev)
        else:
            return root

            
# How to smartly reuse the delete_node function for the delete the left_most leaf of right tree
# Better than this (GFG uses node.val to delete, so there is double search)
# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

# But delete_node function seems too verbose, especialy from block 27