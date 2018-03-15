class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ranges = [(lower, upper)]
        for num in nums:
            if num < lower or num > upper:
                continue
            
            if not ranges:
                # possible due to duplicated elements
                continue
                
            # Corner case that num == e or num == s
            s, e = ranges.pop()
            if s <= num - 1:
                ranges.append((s, num - 1))
            if num + 1 <= e:
                ranges.append((num + 1, e))
        
        return [str(r[0]) if r[0] == r[1] else str(r[0]) + "->" + str(r[1]) for r in ranges] 