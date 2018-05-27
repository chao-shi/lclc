class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cnt_dict = {}
        for ch in secret:
            cnt_dict[ch] = cnt_dict.get(ch, 0) + 1
        
        bull_cow = 0
        bull = 0
        for i, ch in enumerate(guess):
            if cnt_dict.get(ch, 0) > 0:
                bull_cow += 1
                cnt_dict[ch] = cnt_dict[ch] - 1
            if ch == secret[i]:
                bull += 1
                
        return str(bull) + "A" + str(bull_cow - bull) + "B"