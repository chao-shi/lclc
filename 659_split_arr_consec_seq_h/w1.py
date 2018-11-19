class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt_map = collections.defaultdict(int)
        uniq_nums = []
        for num in nums:
            cnt_map[num] += 1
            if cnt_map[num] == 1:
                uniq_nums.append(num)

        for i in range(len(uniq_nums)):
            num_i_cnt = cnt_map[uniq_nums[i]]

            if num_i_cnt == 0:
                continue

            j = i + 1
            while j < len(uniq_nums):
                num_j1, num_j = uniq_nums[j-1], uniq_nums[j]
                if num_j - num_j1 > 1 or cnt_map[num_j] < cnt_map[num_j1]:
                    break
                j += 1
            
            if j - i < 3:
                return False

            for k in range(i, j):
                cnt_map[uniq_nums[k]] -= num_i_cnt
                
            #print cnt_map

        return True
            
# Does not pass case of [1,2,2,2,3,3,3,4,4,5]
# Here we assume there can be only one unique type of sequence from i, which is not true in above case
# 1, 2, 3, 
# 2, 3, 4
# 2, 3, 4, 5

# Line 31 is wrong !!!