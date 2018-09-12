# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def preorder(root, res):
            if root == None:
                return
            res.append(str(root.val))
            preorder(root.left, res)
            preorder(root.right, res)
        
        preorder(root, res)
        return ",".join(res)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            # map function will execption 
            return None

        pre_order = map(int, data.split(","))
        in_order = sorted(pre_order)
        
        in_order_map = {v:i for i, v in enumerate(in_order)}
        
        def reconstruct(i1, j1, i2, j2):
            if i1 == j1:
                return None
            mid = in_order_map[pre_order[i1]]
            left_size = mid - i2
            right_size = j2 - mid - 1
            
            root = TreeNode(pre_order[i1])
            root.left = reconstruct(i1 + 1, i1 + 1 + left_size, i2, mid)
            root.right = reconstruct(i1 + 1 + left_size, j1, mid + 1, j2)
            return root
        
        return reconstruct(0, len(pre_order), 0, len(in_order))
            
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))