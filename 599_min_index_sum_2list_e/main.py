class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_sum = len(list1) + len(list2)
        res = []
        idx_map1 = {r:i for i, r in enumerate(list1)}
        for i, r in enumerate(list2):
            if r in idx_map1:
                idx_sum = i + idx_map1[r]
                if idx_sum == min_sum:
                    res.append(r)
                elif idx_sum < min_sum:
                    min_sum = idx_sum
                    res = [r]
        return res