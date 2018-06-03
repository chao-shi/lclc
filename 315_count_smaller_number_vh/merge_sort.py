class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = [0] * len(nums)
        tuples = list(enumerate(nums))
        
        def sort_and_count(tuples, start, end):
            if end - start < 2:
                return
            mid = (start + end) / 2
            sort_and_count(tuples, start, mid)
            sort_and_count(tuples, mid, end)
            merge(tuples, start, end, mid)
            
        # Merge aim to increment update the left half with right half
        def merge(tuples, start, end, mid):
            aux = [(0, 0)] * (end - start)
            i, j = start, mid
            for k in range(end - start):
                if i == mid:
                    aux[k] = tuples[j]
                    j += 1
                elif j == end:
                    aux[k] = tuples[i]
                    i += 1
                # Don't include equal here
                elif tuples[i][1] > tuples[j][1]:
                    aux[k] = tuples[i]
                    counts[tuples[i][0]] += end - j
                    i += 1
                else:
                    aux[k] = tuples[j]
                    j += 1
            
            tuples[start:end] = aux
        
        
        sort_and_count(tuples, 0, len(nums))
        return counts
        
                    
# The core idea is that during the merge process.
# The correponding right half side of counts is already up to date
# There are still some work for the left side.

# E.G [5, 1, 2, 6], keep the original index as well, it becomes
# [[(0, 5), (1, 1), (2, 2), (6, 3)]

# After sorting two halves becomes
# [(0, 5), (1, 1) || (3, 6), (2, 2)]

# Now do the merge
# The first to go is (3, 6), which is from right side, nothing to update (Right work already done)

# Then (0, 5), from left. 
# since counts[0] already updated with the smaller values on left side
# we just need to know how many on the right half are smaller

# The answer to that is end - j
# Increment on line 32.
