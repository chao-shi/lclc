class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        lower, upper = min(nums), max(nums)

        # Bucket size formula
        # float(max + 1 - min) / (bucket_num)
        # min will be start of the first bucket and max will be end of last bucket
        # 
        # By putting things into N + 1 buckets, we can guarantee some empty bucket
        # [min, ), [, ) .... [ ), [max + 1, )
        # ----------------------
        #    N + 1 buckets here
        #    
        # Only exception is that all values are equal, 
        # they all end up within one bucket
        # this can be solved by initializing
        # 0

        bucket_num = len(nums) + 1
        buckets = collections.defaultdict(lambda : [sys.maxint, -sys.maxint])
        bucket_gap = float(upper+1-lower) / (bucket_num)
        
        for num in nums:
            bucket_idx = int(float(num - lower) / bucket_gap)
            buckets[bucket_idx][0] = min(buckets[bucket_idx][0], num)
            buckets[bucket_idx][1] = max(buckets[bucket_idx][1], num)

        # Only need to check between adjacent buckets. No need to check with same bucket
        maxgap = 0
        # bucket 0 for sure has something, min is there
        last_bucket_idx = 0
        for bucket_idx in range(1, bucket_num):
            if bucket_idx in buckets:
                # Not a empty one
                maxgap = max(maxgap, buckets[bucket_idx][0] - buckets[last_bucket_idx][1])
                last_bucket_idx = bucket_idx
        return maxgap