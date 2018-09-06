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
        def max_branch(root):
            if not root:
                return 0
            return max([len(root.children)] + [max_branch(ch) for ch in root.children])

        n = max_branch(root)

        def recur(root):
            if not root:
                return ["#"]

            ret = [str(root.val)]

            children = root.children
            if len(children) < n:
                children = children + [None] * (n - len(children))
            
            for ch in children:
                ret.extend(recur(ch))
            return ret
        
        return ",".join([str(n)] + recur(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        nodes = data.split(",")
        n, nodes = int(nodes[0]), nodes[1:]
        
        def recur(i):
            if i == len(nodes) or nodes[i] == "#":
                return None, i + 1
            
            root_val = nodes[i]
            children = []
            i += 1
            for _ in range(n):
                child, i = recur(i)
                if child != None:
                    children.append(child)

            root = Node(int(root_val), children)
            return root, i
        
        return recur(0)[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Better solution: Store the branch size right after node value
# This is not best approach, if there is only 1 child out of n, it 
# does not care where is that child. This is the difference from BT.