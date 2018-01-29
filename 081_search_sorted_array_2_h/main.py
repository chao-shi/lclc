class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lb, hb = 0, len(nums) - 1
        while lb <= hb:
            mid = (lb + hb) / 2
            if nums[mid] == target:
                return True

            if nums[mid] != nums[lb]:
                if nums[lb] <= target < nums[mid] or nums[mid] < nums[lb] <= target or target < nums[mid] < nums[lb]:
                    hb = mid - 1
                else:
                    lb = mid + 1
            elif nums[mid] != nums[hb]:
                if nums[mid] < target <= nums[hb] or nums[hb] < nums[mid] < target or target <= nums[hb] < nums[mid]:
                    lb = mid + 1
                else:
                    hb = mid - 1
            else:
                lb, hb = lb + 1, hb - 1
        return False
    
# Good idea to focus on each half. Find the half which boundary does not equal. 
                