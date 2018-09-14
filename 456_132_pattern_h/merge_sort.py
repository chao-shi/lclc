class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_right_smaller = self.cal_max_right_smaller(nums)
        left_smallest = self.cal_left_smallest(nums)
        
        for j in range(1, len(nums) - 1):
            v_i = left_smallest[j]
            v_k = max_right_smaller[j]
            if v_i != None and v_k != None and v_i < v_k < nums[j]:
                return True
        return False
        
        
    def cal_left_smallest(self, nums):
        left_smallest = []
        min_v = None
        for i in range(len(nums)):
            left_smallest.append(min_v)
            min_v = min(min_v, nums[i]) if min_v != None else nums[i]
        return left_smallest
    
    
    def cal_max_right_smaller(self, nums):
        res = [None] * len(nums) 

        idx_nums = list(enumerate(nums))

        def recur(s, t):
            if t - s < 2:
                return
            mid = (s + t) / 2
            recur(s, mid)
            recur(mid, t)
            
            tmp = []
            i, j = s, mid
            for k in range(t - s):
                if i == mid:
                    tmp.append(idx_nums[j])
                    j += 1
                elif j == t:
                    tmp.append(idx_nums[i])
                    i += 1
                elif idx_nums[i][1] <= idx_nums[j][1]:
                    tmp.append(idx_nums[i])
                    i += 1
                else:
                    res[idx_nums[i][0]] = max(res[idx_nums[i][0]], idx_nums[j][1])
                    tmp.append(idx_nums[j])
                    j += 1
            idx_nums[s:t] = tmp
        
        recur(0, len(idx_nums))
        return res