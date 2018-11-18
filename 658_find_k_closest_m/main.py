class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        idx = bisect.bisect_left(arr, x)
        # arr[idx] >= x and arr[idx-1] < x
        i, j = idx - 1, idx
        while j - i - 1 < k:
            if i < 0:
                j += 1
            elif j == len(arr):
                i -= 1
            # smaller element preferred
            elif abs(arr[i] - x)  <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1
        return arr[i+1:j]
        