class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = map(int, list(str(num)))
        n = len(num)

        # This keeps the index of largest element on its right, if multiple equal,
        # Keep the rightmost
        max_right_idx = [None] * n
        max_idx = n - 1
        for i in range(n - 2, -1, -1):
            max_right_idx[i] = max_idx
            if num[i] > num[max_idx]:
                max_idx = i

        # Find the first to swap
        for i in range(n-1):
            if num[max_right_idx[i]] > num[i]:
                num[i], num[max_right_idx[i]] = num[max_right_idx[i]], num[i]
                break
        return int("".join(map(str, num)))
    
# My solution is better than suggested, the suggested has complexity factor of 0-9. 