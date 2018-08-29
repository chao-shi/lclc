class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.spellings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        # solve using linear equations. There are 10 variables and more than 10 constraints.
        scounter = collections.Counter(s)
        x = [0] * 10
        x[0] = scounter['z']
        x[2] = scounter['w']
        x[4] = scounter['u']
        x[6] = scounter['x']
        x[8] = scounter['g']
        x[5] = scounter['f'] - x[4]
        x[7] = scounter['v'] - x[5]
        x[3] = scounter['h'] - x[8]
        x[1] = scounter['o'] - x[0] - x[2] - x[4]
        x[9] = (scounter['n'] - x[1] - x[7]) / 2
        
        digits = [str(i) * x[i] for i in range(10)]
        return "".join(digits)
        