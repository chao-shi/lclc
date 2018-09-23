# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        
        def rand2():
            while True:
                n = rand7()
                if n != 7:
                    return n % 2
        
        def rand14():
            r2 = rand2()
            n = rand7()
            if r2:
                n += 7
            return n
        
        while True:
            n = rand14()
            if n <= 10:
                return n
        
            