class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = []
        cnt = 0
        for num in nums:
            target = 2 * num
            idx = bisect.bisect_right(sorted_nums, target)
            cnt += len(sorted_nums) - idx
            idx = bisect.bisect_right(sorted_nums, num)
            sorted_nums.insert(idx, num)
        return cnt

# passes with 3000ms
# Can be improved by using BST to store sorted_nums