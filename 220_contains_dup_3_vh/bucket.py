class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums:
            return False
        if t < 0:
            # stupid test case
            # This breaks divisor of t + 1
            return False

        minv, maxv = min(nums), max(nums)
        # Important here
        bucket_gap = t + 1
        bucket_cnt = (maxv - minv) / bucket_gap + 1
        # buckets = [{} for i in range bucket_cnt]
        # Cannot more than one element for the bucket of the current window
        buckets = [None for i in range(bucket_cnt)]

        
        def assign_bucket(num):
            buckets[(num - minv) / bucket_gap] = num

        def remove_bucket(num):
            buckets[(num - minv) / bucket_gap] = None
            
        def find_bucket(num):
            return (num - minv) / bucket_gap

        i = 0
        assign_bucket(nums[0])
        for j in range(1, len(nums)):
            if j - i > k:
                remove_bucket(nums[i])
                i += 1
            
            bucket_idx = find_bucket(nums[j])
            if buckets[bucket_idx] != None:
                return True
            elif bucket_idx + 1 < len(buckets):
                up = buckets[bucket_idx + 1]
                if up != None and up - nums[j] <= t:
                    return True
            elif bucket_idx - 1 >= 0:
                down = buckets[bucket_idx - 1]
                if down != None and nums[j] - down <= t:
                    return True
            
            assign_bucket(nums[j])
            