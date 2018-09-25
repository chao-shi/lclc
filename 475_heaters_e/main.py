class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if not heaters:
            return None
        heaters, houses = sorted(heaters), sorted(houses)
        j = -1
        max_radius = 0
        for i, h in enumerate(houses):
            while j + 1 < len(heaters) and heaters[j + 1] <= h:
                j += 1
            
            # heaters[j] is largest heaters on or left to house h
            min_radius = sys.maxint
            if j >= 0:
                min_radius = min(min_radius, h - heaters[j])
            if j + 1 < len(heaters):
                min_radius = min(min_radius, heaters[j+1] - h)
            max_radius = max(max_radius, min_radius)
        return max_radius