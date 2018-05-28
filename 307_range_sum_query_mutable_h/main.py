class SegTreeNode(object):
    def __init__(self, start, end, sum):
        self.start, self.end, self.sum = start, end, sum
        self.left, self.right = None, None

class SegTree(object):
    def __init__(self, nums):
        self.nums = nums
        sum_acc = [0]
        for num in nums:
            sum_acc.append(sum_acc[-1] + num)
        
        self.sum_acc = sum_acc
        self.root = self.make_node(0, len(nums))
    
    def range_sum(self, start, end):
        return self.query_node(self.root, start, end)

    def update(self, index, num):
        self.update_node(self.root, index, num)
        self.nums[index] = num
        
    # Move out to class level to pass OJ
    def make_node(self, start, end):
        if start == end:
            return None

        root = SegTreeNode(start, end, self.sum_acc[end] - self.sum_acc[start])

        # Only if more than one element here
        if end - start > 1:
            mid = (start + end) / 2
            root.left = self.make_node(start, mid)
            root.right = self.make_node(mid, end)

        return root

    def query_node(self, root, start, end):
        # Optional to check if start < root.start or end > root.end
        # Not needed for OJ
        if not root or root.start > root.end:
            return 0
        elif root.start == start and root.end == end:
            return root.sum
        else:
            mid = (root.start + root.end) / 2
            return self.query_node(root.left, start, min(end, mid)) + self.query_node(root.right, max(start, mid), end)
    
    def update_node(self, root, index, num):
        if root and root.start <= index < root.end:
            root.sum += num - self.nums[index]
            self.update_node(root.left, index, num)
            self.update_node(root.right, index, num)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.seg_tree = SegTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.seg_tree.update(i, val)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.seg_tree.range_sum(i, j + 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

# Recursion end is end - start == 1 not zero in make node

# Stupid OJ relies on constant factors. This solution does not pass OJ as 5/28/2018. To pass it, add if condition 
# in places lieke 47 and 51 to reduce the recursion calls

# Update and query complexity is logN