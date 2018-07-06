class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mins = []
        for num in nums:
            if len(mins) == 2 and num > mins[1]:
                return True
            i = 0
            while i < len(mins) and num > mins[i]:
                i += 1
            if i == len(mins):
                mins.append(num)
            elif i < len(mins):
                mins[i] = num
        return False