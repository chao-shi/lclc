class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        def cnt_insert(i, j):
            if j - i < 4:
                return False
            return (j - i) / 2 - 1
        
        # Note the start index need to be -2 and len + 1, 
        # If array is 00001, then first 0 can be put flower
        idx1 = [-2] + [i for i in range(len(flowerbed)) if flowerbed[i] == 1] + [len(flowerbed) + 1]
        cnt = 0
        for i in range(1, len(idx1)):
            cnt += cnt_insert(idx1[i-1], idx1[i])
        return n <= cnt
    