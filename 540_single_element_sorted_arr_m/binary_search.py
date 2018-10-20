class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lb, hb = 0, len(nums) - 1
        # Continue if equal or more than 3 elements
        while lb + 2 <= hb :
            mid = (lb + hb) / 2
            num = nums[mid]
            if nums[mid-1] != num and nums[mid+1] != num:
                return nums[mid]
            
            if nums[mid - 1] == num:
                if (mid - lb - 1) % 2 == 1:
                    # left is odd after removing mid and mid - 1
                    hb = mid - 2
                else:
                    lb = mid + 1
            else:
                if (mid - lb) % 2 == 1:
                    hb = mid - 1
                else:
                    lb = mid + 2
        return nums[lb]
    
# Check middle and check which side is odd, everytime the length of search array reduce by 2. 
# Base case is when array size is 1.
        
        
# Binary search