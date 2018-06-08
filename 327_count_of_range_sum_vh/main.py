class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        self.count = 0
        def merge_sort(sums, start, end):
            if end - start <= 1:
                return
            mid = (start + end) / 2
            merge_sort(sums, start, mid)
            merge_sort(sums, mid, end)
            
            i, j = start, mid
            # Looks complicated, but this is just the regular two pointer approach
            # Two pointers for (p_upper, j) and two pointers for (p_lower, j)
            p_upper, p_lower = start, start
            new_sums = []

            for k in range(start, end):
                # Normal as usualy if pick left
                if j == end or (i < mid and sums[i] < sums[j]):
                    new_sums.append(sums[i])
                    i += 1
                else:
                    # window of (p_upper, p_lower)
                    # where sums[j] - sums[p_upper] <= upper
                    # and sums[j] - sums[p_lower - 1] >= lower
                    # p_upper is first index such that sums[j] - sums[index] <= upper
                    # p_lower is first index such that sums[j] - sums[index] < index
                    # as j moves right, both moves right
                    while p_upper < mid and sums[j] - sums[p_upper] > upper:
                        p_upper += 1
                    while p_lower < mid and sums[j] - sums[p_lower] >= lower:
                        p_lower += 1
                    
                    # valid range is (p_upper, p_lower)
                    self.count += p_lower - p_upper
                        
                    new_sums.append(sums[j])
                    j += 1
                    
            sums[start:end] = new_sums
        
        
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        merge_sort(sums, 0, len(sums))
        return self.count
            

            
# Using the example given by description.
# The sum will be [0, -2, 3, 2]
# After the merge sort on two halves will be [0, -2 || 2, 3]

# Unlike Q315. No need to store original index because only total count is needed
# For first element 2 in second half. Easy to know how many on the first half are inside
# [2 - lower, 2 - higher] because left is sorted. Also right is sorted, so I can use two points 
# m and n here