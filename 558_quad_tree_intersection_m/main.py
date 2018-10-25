"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        # def depth(root):
        #     if root.isLeaf:
        #         return 1
        #     else:
        #         return max(depth(root.topLeft), depth(root.topRight), depth(root.bottomLeft), depth(root.bottomRight)) + 1
        
        q1, q2 = quadTree1, quadTree2
        if q1.isLeaf and q1.val or q2.isLeaf and not q2.val:
            return q1
        elif q1.isLeaf and not q1.val or q2.isLeaf and q2.val:
            return q2
        else:
            tl, tr, bl, br = (self.intersect(q1.topLeft, q2.topLeft), self.intersect(q1.topRight, q2.topRight), 
                              self.intersect(q1.bottomLeft, q2.bottomLeft), self.intersect(q1.bottomRight, q2.bottomRight))
            
            # TT   AND  FF
            # FF        TT 
            # Need to merge
            if tl.isLeaf == tr.isLeaf == bl.isLeaf == br.isLeaf == True and tl.val == tr.val == bl.val == br.val:
                return Node(bl.val, True, None, None, None, None)
            else:
                return Node(None, False, tl, tr, bl, br)
            
# Important thing is that they represent same size matrix
# If a node is leaf and its counterpart is not, we know the answer immediately based on value of the leaf node