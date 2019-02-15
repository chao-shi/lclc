class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def split(nums, start, end):
            rand_pivot = random.randint(start, end - 1)
            nums[start], nums[rand_pivot] = nums[rand_pivot], nums[start]
            j = start + 1
            for i in range(start + 1, end):
                if nums[i] <= nums[start]:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[j-1], nums[start] = nums[start], nums[j-1]
            return j - 1

        def recur(nums, start, end, k):
            if end - start == 1:
                return nums[start]
            sp = split(nums, start, end)
            # k is one base
            if k == sp:
                return nums[sp]
            elif k > sp:
                return recur(nums, sp + 1, end, k)
            else:
                return recur(nums, start, sp, k)
            
        return recur(nums, 0, len(nums), len(nums) - k)

# Difference from main is that recur(...k) k is the global index, not index between [start, end)