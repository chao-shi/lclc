class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        counter = collections.Counter(ages)
        cntv = 0
        for a1 in counter:
            for a2 in counter:
                if not (a2 <= a1 * 0.5 + 7) and \
                       not (a2 > a1) and \
                       not (a2 > 100 and a1 < 100):
                        cntv += counter[a1] * counter[a2]
                        if a1 == a2:
                            cntv -= counter[a1]
        return cntv
                    