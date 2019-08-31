class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(T)
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cold_idx = stack.pop()
                res[cold_idx] = i - cold_idx
            stack.append(i)
        return res