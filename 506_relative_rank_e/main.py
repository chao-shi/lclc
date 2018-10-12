class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def medal(rank):
            if rank < 3:
                return ["Gold Medal", "Silver Medal", "Bronze Medal"][rank]
            else:
                return str(rank + 1)
        rank_map = {num:i for i, num in enumerate(sorted(nums, reverse=True))}
        
        return [medal(rank_map[num]) for num in nums]
            