class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid(s):
            left_cnt = 0
            for ch in s:
                if ch == '(':
                    left_cnt += 1
                elif ch == ')':
                    left_cnt -= 1
                if left_cnt < 0:
                    return False
            return left_cnt == 0
        
        level = set([s])
        while level:
            valids = filter(valid, level)
            if valids:
                return list(valids)

            new_level = set()
            for ss in level:
                for i in range(len(ss)):
                    if ss[i] == "(" or ss[i] == ")":
                        new_level.add(ss[:i] + ss[i+1:])
            level = new_level
        
        # Why letter matters
        # Case of (a() which will return [a(), (a)]
        
        