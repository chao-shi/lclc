# Line 38 under remove: very important

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hm = {}
        self.arr = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        newValue = val not in self.hm
        self.arr.append(val)
        if newValue:
            self.hm[val] = set()
        self.hm[val].add(len(self.arr) - 1)
        return newValue
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hm:
            return False

        idx = self.hm[val].pop()
        self.arr[idx] = self.arr[-1]
        if idx != len(self.arr) - 1:
            self.hm[self.arr[idx]].remove(len(self.arr) - 1)
            self.hm[self.arr[idx]].add(idx)
        self.arr.pop()
        
        # Don't forget to clean here
        if not self.hm[val]:
            del self.hm[val]

        return True
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if not self.arr:
            return None
        return self.arr[random.randint(0, len(self.arr)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()