class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        vol = 0
        peak = height.index(max(height))
        highest = 0
        for i in range(peak + 1):
            if height[i] < highest:
                # here we know we have highest on the left
                # and we for sure have something no smaller 
                # than highest on the right (because we haven't reach
                # mid point yet). So highest - height[i] is guaranteed
                vol += highest - height[i]
            else:
                # we update highest even it is equal
                # because same height separate the water body
                highest = height[i]
        
        highest = 0
        for i in range(len(height) - 1, peak - 1, -1):
            if height[i] < highest:
                vol += highest - height[i]
            else:
                highest = height[i]
        
        return vol