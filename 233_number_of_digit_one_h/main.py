class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        n += 1
        # base_map stores
        # (0, 1)    how many 1: 0
        # (0, 10)   how many 1: 0 * 10 + 1 = 1
        # (0, 100)  how many 1: 1 * 10 + 10 = 20
        # (0, 1000) how many 1: 20 * 10 + 100 = 300
        base_map = {1: 0}
        base = 10
        while base <= n:
            base_map[base] = base_map[base/10] * 10 + base / 10
            base *= 10

        # For example n = 456
        # (0, 456) = (0, 400) + (400, 450) + (450, 456)
        # Look at digit by digit
        base = 1
        cnt = 0
        digits = map(int, list(str(n)))
        
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            
            # Digits 1 after current digit
            cnt += digit * (base_map[base])
            
            # Digits 1 before
            cnt += digit * base * digits[:i].count(1)
            
            # Count current digit for 1
            if digit > 1:
                cnt += base
                
            base *= 10
        return cnt