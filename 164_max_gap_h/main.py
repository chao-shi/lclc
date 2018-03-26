class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        # need to +1 to make sure max(nums) fits inside the bucket, not on the boundary
        lower, upper = min(nums), max(nums) + 1

        # problem of saving to set, only a problem when all elements are equal.
        # Passes the insideBucket function
        load_factor = 5
        bucket_num = len(nums) / load_factor + 1
        buckets = [[] for i in range(bucket_num)]
        bucket_gap = float(upper-lower) / float(bucket_num)
        
        for num in nums:
            bucket_idx = int(float(num - lower) / bucket_gap)
            buckets[bucket_idx].append(num)
        
        maxgap = None
        last_nonempty = None
        for i in range(bucket_num):
            if len(buckets[i]) > 0:
                if last_nonempty != None:
                    maxgap = max(maxgap, -max(buckets[last_nonempty]) + min(buckets[i]))
                maxgap = max(maxgap, self.insideBucket(buckets[i]))
                last_nonempty = i
        
        return maxgap
    
    def insideBucket(self, nums):
        nums = sorted(nums)
        maxgap = None
        for i in range(1, len(nums)):
            maxgap = max(maxgap, nums[i] - nums[i-1])
        return maxgap