class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = map(int, list(str(N)))
        decr_ptr = None
        for i in range(1, len(num)):
            if num[i] < num[i-1]:
                decr_ptr = i
                break
    
        if decr_ptr:
            # 332 and 342 case
            # Need to go back
            decr_ptr -= 1
            while decr_ptr > 0 and num[decr_ptr] == num[decr_ptr-1]:
                decr_ptr -= 1
            num[decr_ptr] -= 1
            for i in range(decr_ptr + 1, len(num)):
                num[i] = 9

        return int("".join(map(str, num)))
                
        