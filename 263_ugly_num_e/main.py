class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=0 :
            return False
        while num > 1:
            flag = False
            for factor in [2, 3, 5]:
                if num % factor == 0:
                    num /= factor
                    flag = True
                    break
                    
            if not flag:
                return False
        return True
            