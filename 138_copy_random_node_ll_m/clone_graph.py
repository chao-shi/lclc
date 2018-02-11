# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        hm = {}
        def copy(node):
            if node == None:
                return None
            elif node in hm:
                return hm[node]
            else:
                newnode = RandomListNode(node.label)
                hm[node] = newnode
                newnode.next = copy(node.next)
                newnode.random = copy(node.random)
                return newnode
        
        return copy(head)

# This is the same approach as iterative with hashmap. 
# Because we are always calling next before random on recursion