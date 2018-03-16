class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ballot = 0
        maj = None
        for num in nums:
            if ballot == 0:
                maj = num
                ballot = 1
            elif num == maj:
                ballot += 1
            else:
                ballot -= 1
        return maj