class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def fizz_buzz(x):
            if x % 15 == 0:
                return "FizzBuzz"
            elif x % 5 == 0:
                return "Buzz"
            elif x % 3 == 0:
                return "Fizz"
            return str(x)
        return map(fizz_buzz, range(1, n + 1))
        