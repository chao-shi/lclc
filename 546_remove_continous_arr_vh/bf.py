class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        self.mt = {}
        
        def recur(boxes):
            if len(boxes) == 0:
                return 0

            elif boxes in self.mt:
                return self.mt[boxes]

            max_v = 0
            j = 0
            for i in range(len(boxes) + 1):
                if i == len(boxes) or boxes[i] != boxes[j]:
                    max_v = max(max_v, (i-j)**2 + recur(boxes[:j] + boxes[i:]))
                    j = i
            self.mt[boxes] = max_v
            return max_v
        
        return recur(tuple(boxes))