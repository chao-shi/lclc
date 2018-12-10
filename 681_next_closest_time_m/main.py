class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def valid(i, digits):
            t, d = i / 10, i % 10
            return t in digits and d in digits
        
        def all_valids(digits):
            res = []
            for i in range(60):
                if valid(i, digits):
                    res.append(i)
            return set(res)
        
        digits = set([int(d) for d in time if d.isdigit()])
        hour, minute = map(int, time.split(":"))
        valids = all_valids(digits)

        min_larger = sorted([v for v in valids if v > minute])
        if min_larger:
            return "{:02d}:{:02d}".format(hour, min_larger[0])
        
        hour_larger = filter(lambda x : x in valids, [(hour + d) % 24 for d in range(1, 25)])
        if hour_larger:
            return "{:02d}:{:02d}".format(hour_larger[0], min(valids))
        
        return None