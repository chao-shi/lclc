class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # This recursion does not take backtrace
        def recur(seq, i):
            if i == len(num) and len(seq) > 2:
                return True
            next_val = seq[-1] + seq[-2]
            next_val_str = str(next_val)
            if num[i:i+len(next_val_str)] == next_val_str:
                seq.append(next_val)
                return recur(seq, i + len(next_val_str))
            return False
        
        for i in range(1, len(num)):
            for j in range(i + 1, len(num) + 1):
                num1, num2 = num[:i], num[i:j]
                if len(num1) > 1 and num1[0] == '0' or len(num2) > 1 and num2[0] == '0':
                    continue
                if recur([int(num1), int(num2)], j):
                    return True
        return False

# Not bad question