class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lb, hb = 0, len(height) - 1
        maxv = 0
        while lb < hb:
            maxv = max(maxv, min(height[lb], height[hb]) * (hb - lb))
            if height[lb] <= height[hb]:
                lb += 1
            else:
                hb -= 1
        return maxv

# equal case does not matter