class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_sum = sum(nums)
        
        if num_sum % k != 0:
            return False
        
        nums = sorted(nums, reverse=True)
        target = num_sum / k
        n = len(nums)

        # Fast indexing of all superset of num[i] which add to target
        combo_map = collections.defaultdict(set)
        for mask in range(2**n):
            mask_str = bin(mask)[2:]
            mask_str = "0" * (n-len(mask_str)) + mask_str
            combo = tuple(ii for ii in range(len(mask_str)) if mask_str[ii] == '1')
            if sum(map(lambda idx:nums[idx], combo)) == target:
                for idx in combo:
                    combo_map[idx].add(combo)
                    
        
        mt = {}
        
        def recur(remain_k, avai_nums):
            mt_tag = (remain_k, tuple(avai_nums))
            if mt_tag in mt:
                return mt[mt_tag]
            elif remain_k == 0:
                return True
            
            # Optmization here, always use smallest index as priority
            must_use = min(avai_nums)
            for combo in combo_map[must_use]:
                if all(idx in avai_nums for idx in combo):
                    for idx in combo:
                        avai_nums.remove(idx)
                    if recur(remain_k-1, avai_nums):
                        mt[mt_tag] = True
                        return True
                    for idx in combo:
                        avai_nums.add(idx)
            mt[mt_tag] = False
            return False
        
        return recur(k, set(range(n)))

# This approach precompute all valid combo with sum equal to target.
# Each time it picks one valild combo from the available numbers which make 

# Not very good, no gauranteed on line 40 complexity. 
# Fix cost of precomputing everything is 2**N
# Recur can go up to N * (2 ** N) * (2 ** N), which is N * 4**N
# Depends on the value of k