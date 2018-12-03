class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Two maps below key is the number.
        cnt_map = collections.defaultdict(int)
        # Easy to code when made it 1
        max_len_map = collections.defaultdict(lambda : 1)
        
        for i, num in enumerate(nums):
            # sequence by itself
            if max_len_map[num] == 1:
                cnt_map[num] += 1

            for last in max_len_map:
                if num > last:
                    if max_len_map[last] + 1 == max_len_map[num]:
                        cnt_map[num] += cnt_map[last]
                    elif max_len_map[last] + 1 > max_len_map[num]:
                        cnt_map[num] = cnt_map[last]
                        max_len_map[num] = max_len_map[last] + 1
        max_len = max(max_len_map.values())        
        return sum(cnt_map[last] for last in max_len_map if max_len_map[last] == max_len)