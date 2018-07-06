class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t1 = None
        t2 = [None, None]
        
        for num in nums:
            if t2[1] != None and t2[1] < num:
                return True

            # Updating t1, t2
            if t1 == None or num < t1:
                t1 = num
            # if t1 just set, then t1 = num, cannot update t2
            # t1 cannot be None here
            if t1 < num and (t2[1] == None or num < t2[1]):
                t2 = [t1, num]
        
        return False
                
            