class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # prefix of length i of number in 32 bit format, 
        def prefix(num, i):
            i = 32 - i
            b = bin(num >> i)[2:]
            prefix = '0' * (32 - i - len(b)) + b
            return prefix

        prefixes = set()
        for num in nums:
            for i in range(1, 33):
                prefixes.add(prefix(num, i))
        
        max_v = 0
        for num in nums:
            prefix = ""
            for i in range(31, -1, -1):
                bit = (num & (1 << i)) >> i
                p1 = prefix + str(1 - bit)
                p2 = prefix + str(bit)
                if p1 in prefixes > 0:
                    prefix = p1
                else:
                    prefix = p2
                # No third case here
            
            max_v = max(max_v, num ^ int(prefix, 2))

        return max_v

# For each number search from most significant bit.
# Search from bit 31 to bit 0
# Try first put the different bit as number on index i, if the prefix formed 
# is valid (line 26), otherwise use line same bit
# 
# Prefix has to be string, otherwise,
# 1 can be both prefix of
# 000001 and 1000000