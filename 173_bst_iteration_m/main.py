# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.moveNext()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None
        node = self.stack[-1]
        self.moveNext()
        return node.val
    
    def moveNext(self):
        if self.stack:
            p = self.stack.pop().right
        else:
            p = self.root
        
        while p:
            self.stack.append(p)
            p = p.left    

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())