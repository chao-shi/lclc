class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt_map = collections.Counter(nums)
        num_arr = [num for i, num in enumerate(nums) if i == 0 or num != nums[i-1]]
        
        # Important, manually add an closing at the end
        num_arr.append(num_arr[-1] + 1)

        # Record how many sequences start at given num_arr[i]
        start_cnt = [0] * len(num_arr)
        start_cnt[0] = cnt_map[num_arr[0]]
        
        j = 0
        for i in range(1, len(num_arr)):
            num = num_arr[i]
            
            if cnt_map[num] > cnt_map[num - 1]:
                # start a few new sequences if num - is missing or smaller count
                start_cnt[i] = cnt_map[num] - cnt_map[num-1]
            
            cnt_closed = 0
            if cnt_map[num] < cnt_map[num - 1]:
                # continuous and smaller
                cnt_closed = cnt_map[num - 1] - cnt_map[num]
            elif num > num_arr[i-1] + 1:
                # Not continous, skipping a few numbers
                cnt_closed = cnt_map[num_arr[i-1]]
        
            # Try to see what to close on, test each j to see if more than 3 apart from num_arr[i-1]
            while cnt_closed > 0:
                if num_arr[i-1] - num_arr[j] < 2:
                    return False
                if cnt_closed >= start_cnt[j]:
                    cnt_closed -= start_cnt[j]
                    start_cnt[j] = 0
                    j += 1
                else:
                    start_cnt[j] -= cnt_closed
                    cnt_closed = 0
        return True