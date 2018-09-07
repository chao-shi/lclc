"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None
        bt_root = TreeNode(root.val)
        bt_sub = map(self.encode, root.children)
        
        if bt_sub:
            for i in range(1, len(bt_sub)):
                bt_sub[i-1].right = bt_sub[i]
            bt_root.left = bt_sub[0]
        
        return bt_root

    # should check if data is null outside calling.
    # Otherwise will have none children in the result N-ary tree
    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        # Only for empty tree
        if not data:
            return None
        
        p = data.left
        children = []
        while p:
            children.append(self.decode(p))
            p = p.right
        return Node(data.val, children)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))