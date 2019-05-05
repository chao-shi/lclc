class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.hm = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hm:
            return False
        self.arr.append(val)
        self.hm[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hm:
            return False
        
        idx = self.hm[val]
        del self.hm[val]
        self.arr[idx] = self.arr[-1]
        if idx != len(self.arr) - 1:
            self.hm[self.arr[idx]] = idx
        self.arr.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.arr)-1)
        return self.arr[idx]

class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.m, self.n = n_rows, n_cols
        self.reset()

    def flip(self):
        """
        :rtype: List[int]
        """
        idx = self.rs.getRandom()
        self.rs.remove(idx)
        return [idx / self.n, idx % self.n]
        

    def reset(self):
        """
        :rtype: void
        """
        self.rs = RandomizedSet()
        for i in range(self.m * self.n):
            self.rs.insert(i)

# Problem is MLE