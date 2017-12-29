class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def reverse_pos(x):
            ret = 0
            while x > 0:
                ret *= 10
                ret += x % 10
                x /= 10
            # careful of << priority
            # what is 32-bit signed biggest
            # 011111...1
            if ret > ((1 << 31) -1):
                return 0
            return ret
        
        if x < 0:
            return - reverse_pos(-x)
        else:
            return reverse_pos(x)