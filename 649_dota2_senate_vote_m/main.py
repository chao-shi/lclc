class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        state = [True] * n
        cr = senate.count("R")
        cd = n - cr
        band, banr = 0, 0

        while True:
            for i in range(n):
                if not state[i]:
                    continue
                elif senate[i] == 'R':
                    if banr > 0:
                        # One point damage for R
                        banr -= 1
                        state[i] = False
                        cr -=1 
                    else:
                        band += 1
                else:
                    if band > 0:
                        band -= 1
                        state[i] = False
                        cd -= 1
                    else:
                        banr += 1
            
            if cr == 0:
                return "Dire"
            elif cd == 0:
                return "Radiant"