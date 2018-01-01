class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        alphas = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ret = [""]
        for ch in digits:
            ret = [comb + letter for letter in alphas[int(ch)] for comb in ret]
        return ret

# test case "123", ""