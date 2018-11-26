class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val_map = {}
        for num in nums:
            val, idx = num % 10, num / 10
            d, col = idx / 10, idx % 10
            val_map[(d, col)] = val
            
        self.path_sum = 0

        def recur(d, col, path):
            if (d, col) not in val_map:
                return
            path += val_map[(d, col)]
            d1, col1, d2, col2 = d + 1, col * 2 - 1, d + 1, col * 2
            if (d1, col1) not in val_map and (d2, col2) not in val_map:
                self.path_sum += path
            recur(d1, col1, path)
            recur(d2, col2, path)
        
        recur(1, 1, 0)
        return self.path_sum