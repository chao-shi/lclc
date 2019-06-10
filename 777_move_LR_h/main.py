class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # if len(start) != len(end):
        #     return False
        # seq1 = [ch for ch in start if ch != 'X']
        # seq2 = [ch for ch in end if ch != 'X']
        # return seq1 == seq2
        # This solution above is for replacing between LX to XL and between RX and XR
        # The question said only XL to LX,
        # RX to XR
        # Feels like L only moves left and R only moves right
        # And L / R does not cross each other.
        
        if len(start) != len(end):
            return False
        seq1 = [(i, ch) for i, ch in enumerate(start) if ch != 'X']
        seq2 = [(i, ch) for i, ch in enumerate(end) if ch != 'X']
        if len(seq1) != len(seq2):
            return False

        for e1, e2 in zip(seq1, seq2):
            i1, ch1 = e1
            i2, ch2 = e2
            if ch1 != ch2 or (ch1 == 'L' and i2 > i1) or (ch1 == 'R' and i2 < i1):
                return False
        return True