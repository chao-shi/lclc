class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # disctinct number
        top3 = set()
        for num in nums:
            top3.add(num)
            if len(top3) > 3:
                top3.remove(min(top3))
        return min(top3) if len(top3) == 3 else max(top3)
    
# Best solution