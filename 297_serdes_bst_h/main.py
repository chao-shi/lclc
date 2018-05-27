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
        def ser_helper(root):
            if not root:
                return ["#"]
            ll = [str(root.val)]
            ll += ser_helper(root.left)
            ll += ser_helper(root.right)
            return ll
        return ",".join(ser_helper(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def des_helper(ll, i):
            if i >= len(ll):
                raise Exception("Parsing error")
            elif ll[i] == "#":
                return None, i + 1
            else:
                root = TreeNode(int(ll[i]))
                left_t, i = des_helper(ll, i + 1)
                right_t, i = des_helper(ll, i)
                root.left, root.right = left_t, right_t
                return root, i
        ll = data.split(",")
        root, i = des_helper(ll, 0)
        if i < len(ll):
            raise Exception("Parsing Error")
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))