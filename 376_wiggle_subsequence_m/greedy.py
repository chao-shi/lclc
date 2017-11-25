class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for num in nums:
            if len(res) < 2:
                if len(res) == 0 or res[-1] != num:
                    res.append(num)
            elif res[-2] > res[-1]:
                if num > res[-1]:
                    res.append(num)
                elif num < res[-1]:
                    res[-1] = num
            else:
                if num > res[-1]:
                    res[-1] = num
                elif num < res[-1]:
                    res.append(num)
        return len(res)

# Careful on if condition of line 10