class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.accu_w = [0]
        for wi in w:
            self.accu_w.append(self.accu_w[-1] + wi)
        
    def pickIndex(self):
        """
        :rtype: int
        """
        r = random.randint(0, self.accu_w[-1] - 1)
        return bisect.bisect_right(self.accu_w, r) - 1
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()