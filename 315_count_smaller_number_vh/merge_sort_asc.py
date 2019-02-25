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
                    counts[tuples[i][0]] += j - mid
                    i += 1
                # Don't include equal here
                elif tuples[i][1] <= tuples[j][1]:
                    aux[k] = tuples[i]
                    counts[tuples[i][0]] += j - mid
                    i += 1
                else:
                    aux[k] = tuples[j]
                    j += 1
            
            tuples[start:end] = aux
        
        
        sort_and_count(tuples, 0, len(nums))
        return counts
        
                    
# How to write if sorting ascending, needs line 29 which desending does not need