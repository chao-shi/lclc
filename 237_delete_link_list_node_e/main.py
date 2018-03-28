# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while True:
            # except tail, node.next always there
            node.val = node.next.val
            if node.next.next == None:
                node.next = None
                break
            else:
                node = node.next