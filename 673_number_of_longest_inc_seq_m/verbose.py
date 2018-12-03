class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1, 3, 5, 8, 10, 6, 5, 6, 7, 8, 9
        # cnt_maps[i] are counterpart, key is last element, value is how many such sequence.
        if not nums:
            return 0

        min_last = [nums[0]]
        cnt_maps = [collections.defaultdict(int)]
        cnt_maps[0][nums[0]] = 1

        for i in range(1, len(nums)):
            idx = bisect.bisect_left(min_last, nums[i])
            if idx < len(min_last):
                min_last[idx] = nums[i]
            else:
                min_last.append(nums[i])
                cnt_maps.append(collections.defaultdict(int))
            
            cnt_maps[0][nums[i]] += 1
            for j in range(idx):
                cnt_map = cnt_maps[j]
                cnt_maps[j+1][nums[i]] += sum(cnt_map[last] for last in cnt_map if last < nums[i])
        return sum(cnt_maps[-1][last] for last in cnt_maps[-1])