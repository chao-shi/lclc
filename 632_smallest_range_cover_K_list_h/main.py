class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if any(len(num) == 0 for num in nums):
            return False

        heap = [(num[0], i, 0) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        maxv = max(num[0] for num in nums)
        min_diff = sys.maxint
        rs, rt = None, None

        while len(heap) == len(nums):
            minv, i, idx = heapq.heappop(heap)
            diff = maxv - minv

            if diff < min_diff or diff == min_diff and minv < rs:
                min_diff = maxv - minv
                rs, rt = minv, maxv

            if idx < len(nums[i]) - 1:
                heapq.heappush(heap, (nums[i][idx+1], i, idx + 1))
                maxv = max(maxv, nums[i][idx+1])
        
        return [rs, rt]