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
            # q2 is the last element on the 2 * nums[q2] < top_of_left
            q2 = mid

            for k in range(j-i):
                if p2 == j or (p1 != mid and nums[p1] <= nums[p2]):
                    while q2 < j and 2 * nums[q2] < nums[p1]:
                        q2 += 1
                    self.cnt += q2 - mid
                    tmp.append(nums[p1])
                    p1 += 1
                else:
                    tmp.append(nums[p2])
                    p2 += 1

            nums[i:j] = tmp
                
        recur(0, len(nums))
        return self.cnt
                
        
# Merge sort
# Full solution see here
# https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22