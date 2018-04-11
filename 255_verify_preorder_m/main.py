class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        under_left_tree = []
        max_popped = None
        for i, num in enumerate(preorder):
            while under_left_tree and under_left_tree[-1] <= num:
                max_popped = max(max_popped, under_left_tree.pop())
            if num <= max_popped:
                return False
            under_left_tree.append(num)
        return True

# under_left_tree stores all values such that we are under its left tree.

# How to do for post order,
# Iterate reversely, use under_right_tree instead and check upper bound.