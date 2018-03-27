class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ranges = [[nums[0], nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] == ranges[-1][1] + 1:
                ranges[-1][1] = nums[i]
            else:
                ranges.append([nums[i], nums[i]])
        return [str(start) + "->" + str(end) if end != start else str(start) for start, end in ranges]