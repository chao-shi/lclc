class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        n = len(x)
        if n <= 3:
            return False
        
        # maintain last six points
        win = [[0, 0], [0,0], [0,0], [0, x[0]], [-x[1], x[0]], [-x[1], x[0] - x[2]]]

        for i in range(3, n):
            if i%4 == 3:
                # going east
                next = [win[-1][0] + x[i], win[-1][1]]
            elif i%4 == 0:
                # going north
                next = [win[-1][0], win[-1][1] + x[i]]
            elif i%4 == 1:
                # going west
                next = [win[-1][0] - x[i], win[-1][1]]
            else:
                # going south
                next = [win[-1][0], win[-1][1] - x[i]]

            # checking crossing line win[0], win[1]
            if checkCrossing(win[-1], next, win[0], win[1]):
                return True

            # checking crossing line win[2], win[3]
            if checkCrossing(win[-1], next, win[2], win[3]):
                return True

            win.pop(0)
            win.append(next)

        return False
        
# line a and line b        
def checkCrossing(a1, a2, b1, b2):
    cpa1 = cross([b1[0] - a1[0], b1[1] - a1[1]], [b2[0] - a1[0], b2[1] - a1[1]])
    cpa2 = cross([b1[0] - a2[0], b1[1] - a2[1]], [b2[0] - a2[0], b2[1] - a2[1]])
    cpb1 = cross([a1[0] - b1[0], a1[1] - b1[1]], [a2[0] - b1[0], a2[1] - b1[1]])
    cpb2 = cross([a1[0] - b2[0], a1[1] - b2[1]], [a2[0] - b2[0], a2[1] - b2[1]])
    
    if cpa1 == 0 and cpa2 == 0 and cpb1 == 0 and cpb2 == 0:
        # four points in a straight line
        return min(b1[0], b2[0]) <= max(a1[0], a2[0]) and max(b1[0], b2[0]) >= min(a1[0], a2[0])
    elif cpa1 * cpa2 <= 0 and cpb1 * cpb2 <= 0:
        return True

    return False
    
def cross(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]