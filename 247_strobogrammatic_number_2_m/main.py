class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        mapping = {
            "6": "9",
            "9": "6",
            "0": "0",
            "1": "1",
            "8": "8"
        }
        
        res = [[""], ["0", "1", "8"]]
        
        for i in range(2, n + 1):
            res.append([k + num + mapping[k] for num in res[i-2] for k in mapping])
        return filter(lambda x: x == "0" or not x.startswith("0"), res[-1])