class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        bag = {}
        counter = collections.Counter(t)
        matched = 0
        i = 0
        minwin = None

        for j, ch in enumerate(s):
            bag[ch] = bag.get(ch, 0) + 1
            if bag[ch] <= counter.get(ch, 0):
                matched += 1
            
            while i <= j:
                if bag[s[i]] > counter.get(s[i], 0):
                    bag[s[i]] = bag[s[i]] - 1
                    i += 1
                else:
                    break
            
            if matched == len(t) and (minwin == None or j - i + 1 < len(minwin)):
                minwin = s[i:j+1]

        return minwin if minwin != None else ""

# Keep bag of all characters, block 16 is critical