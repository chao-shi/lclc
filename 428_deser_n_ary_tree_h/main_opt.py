"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def recur(root, res):
            if not root:
                res.append("#")
            else:
                res.append(root.val)
                for child in root.children:
                    recur(child, res)
                res.append("#")

        res = []
        recur(root, res)
        return ",".join(map(str, res))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        tokens = data.split(",")

        def recur(i):
            if tokens[i] == "#":
                return None, i+1
            root = Node(int(tokens[i]), [])
            i += 1
            while True:
                ch, i = recur(i)
                if ch:
                    root.children.append(ch)
                else:
                    break
            return root, i

        return recur(0)[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Better solution: Store the branch size right after node value
# This is not best approach, if there is only 1 child out of n, it 
# does not care where is that child. This is the difference from BT.