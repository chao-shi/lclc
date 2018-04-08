class Solution(object):
    
    def generateList(self, n):
        mapping = {
            "6": "9",
            "9": "6",
            "0": "0",
            "1": "1",
            "8": "8"
        }
        res = [[""], ["0", "1", "8"]]
        for i in range(2, n+1):
            res.append([k + num + mapping[k] for num in res[i-2] for k in sorted(mapping.keys())])
        return res

    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        # Stupid OJ case
        if len(low) > len(high):
            return 0
        
        res = self.generateList(len(high))

        def count_lower(num, include=False):
            n = len(num)
            if n == 1:
                return len(filter(lambda x : x <= num if include else x < num, res[n]))
            else:
                # res[2:n] needs to * 0.8 to remove zero leading numbers
                cnt = 3 + sum(map(len, res[2:n])) * 4 / 5
                
                # How many numbers with length n smaller than num
                cnt += len(filter(lambda x : x <= num if include else x < num, res[n]))

                # Remove the mistaken count of zero leadings
                cnt -=len(res[n]) / 5
                return cnt

        return count_lower(high, include=True) - count_lower(low)

# No good solution. Need enumeation and iterate on the same length.
# Bad question