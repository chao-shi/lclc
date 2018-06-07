class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        def find_median(nums):
            nums = sorted(nums)
            n = len(nums)
            if n % 2 == 1:
                return nums[n/2]
            else:
                return nums[n/2 - 1]

        # https://en.wikipedia.org/wiki/Dutch_national_flag_problem#Pseudocode
        def dutch_flag(nums, median):
            i, j, k = 0, 0, len(nums) - 1
            while j <= k:
                if nums[j] < median:
                    nums[i], nums[j] = nums[j], nums[i]
                    i, j = i + 1, j + 1
                elif nums[j] == median:
                    j += 1
                else:
                    nums[j], nums[k] = nums[k], nums[j]
                    k -= 1
                    
        median = find_median(nums)
        dutch_flag(nums, median)

        # M  M  S  S
        #   L  L  M
        new_nums = [0] * len(nums)
        j = len(nums) - 1
        for i in range(1, len(nums), 2):
            new_nums[i] = nums[j]
            j -= 1

        for i in range(0, len(nums), 2):
            new_nums[i] = nums[j]
            j -= 1

        nums[:] = new_nums
        
# The Partial idea of
# https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/Step-by-step-explanation-of-index-mapping-in-Java

# O(N) time complexity (Needs to implement linear order functino for find_median)
# O(N) extra space

# O(1) needs virtual indexing