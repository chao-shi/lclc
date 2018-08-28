class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxxor = 0
        for i in range(32)[::-1]:
            prefixes = {num >> i for num in nums}
            maxxor <<= 1
            # search for (maxxor << 1) + 1
            for p in prefixes:
                # a ^ x = b how to get x
                # x = a^b
                if p ^ (maxxor + 1) in prefixes:
                    maxxor += 1
        return maxxor