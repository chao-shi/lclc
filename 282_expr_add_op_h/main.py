class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        def recur(i, prefix, prefix_sum, prefix_term):
            if i == len(num) and prefix_sum == target:
                res.append(prefix)
                return
            for j in range(i + 1, len(num) + 1):
                # Skip for leading zero
                if j - i > 1 and num[i] == '0':
                    break
                term = int(num[i:j])

                recur(j, prefix + "+" + num[i:j], prefix_sum + term, term)
                recur(j, prefix + "-" + num[i:j], prefix_sum - term, -term)
                recur(j, prefix + "*" + num[i:j], prefix_sum + (term - 1) * prefix_term, term * prefix_term)
        
        for i in range(1, len(num) + 1):
            if i > 1 and num[0] == '0':
                break
            recur(i, num[:i], int(num[:i]), int(num[:i]))
        
        return res