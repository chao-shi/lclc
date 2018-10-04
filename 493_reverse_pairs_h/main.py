class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.cnt = 0

        def recur(i, j):
            if j - i <= 1:
                return

            mid = (i + j) / 2
            recur(i, mid)
            recur(mid, j)

            tmp = []
            p1, p2 = i, mid
            # q1 is the first element on the left <= 2 * top_of_right
            q1 = i

            for k in range(j-i):
                if p1 == mid or (p2 != j and nums[p1] <= nums[p2]):
                    while q1 < mid and nums[q1] > 2 * nums[p2]:
                        q1 += 1
                    self.cnt += q1 - i
                    tmp.append(nums[p2])
                    p2 += 1
                else:
                    tmp.append(nums[p1])
                    p1 += 1

            nums[i:j] = tmp
                
        recur(0, len(nums))
        return self.cnt
                
        
# Merge sort
# Full solution see here
# https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22