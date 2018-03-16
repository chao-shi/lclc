class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.counter[number] = self.counter.get(number, 0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n1 in self.counter.keys():
            n2 = value - n1
            if n2 != n1 and n2 in self.counter:
                return True
            elif n2 == n1 and self.counter[n1] > 1:
                return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# Using dictionary is always superior to sorting. Since you pick the data structure. Both of them use O(N)
# memory. The in place advantage of sorting no longer exists

# Here add is O(1), find is O(N)
# To tradeoff add is O(N), find is O(1)

# Usually there much less find. If find is smaller than total N. This approach above is better 