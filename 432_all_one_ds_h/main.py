class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.first_idx = {}
        self.last_idx = {}
        
        self.key_map = {}
        self.arr = []
        

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        #print "inc", key
        #print self.first_idx, self.last_idx, self.arr, self.key_map
        if key not in self.key_map:
            self.arr.append([1, key])
            # Don't forget here
            if 1 not in self.last_idx:
                self.first_idx[1] = len(self.arr) - 1
            self.last_idx[1] = len(self.arr) - 1
            self.key_map[key] = len(self.arr) - 1
        else:
            j = self.key_map[key]
            val = self.arr[j][0]
            i = self.first_idx[val]
            
            # swap i, j
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.key_map[self.arr[i][1]] = i
            self.key_map[self.arr[j][1]] = j
            
            # increment i
            self.arr[i][0] = val + 1
            
            # adjust idx map for val
            if self.first_idx[val] == self.last_idx[val]:
                del self.first_idx[val]
                del self.last_idx[val]
            else:
                self.first_idx[val] += 1
            
            # adjust idx map for val + 1
            if val + 1 not in self.last_idx:
                self.first_idx[val + 1] = i
            self.last_idx[val + 1] = i
            
            

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        #print "dec", key
        #print self.first_idx, self.last_idx, self.arr, self.key_map

        if key not in self.key_map:
            return
        else:
            j = self.key_map[key]
            val = self.arr[j][0]
            i = self.last_idx[val]
            
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.key_map[self.arr[i][1]] = i
            self.key_map[self.arr[j][1]] = j
            
            if val == 1:
                self.arr.pop()
                del self.key_map[key]
            else:
                self.arr[i][0] = val - 1
                
            if self.first_idx[val] == self.last_idx[val]:
                del self.first_idx[val]
                del self.last_idx[val]
            else:
                self.last_idx[val] -= 1
            
            if val - 1 not in self.first_idx:
                self.last_idx[val - 1] = i
            self.first_idx[val - 1] = i

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if not self.arr:
            return ""
        return self.arr[0][1]
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if not self.arr:
            return ""
        return self.arr[-1][1]
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# Key point is to keep the last and first idx of certain value
# When we incr, look at the first idx for that value and swap
# vice versa.
# 
# Easier implementation use treemap to index the values. 
# But not O(1)