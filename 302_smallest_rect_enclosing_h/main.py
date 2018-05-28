class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])
        def firstBad(i, j, target, isCol):
            lb, hb = i, j
            while lb <= hb:
                mid = (lb + hb) / 2
                if isCol:
                    proj = 1 if any(image[k][mid] == "1" for k in range(m)) else 0
                else:
                    proj = 1 if any(image[mid][k] == "1" for k in range(n)) else 0

                if proj == target:
                    # bad version
                    hb = mid - 1
                else:
                    lb = mid + 1
            return lb
        
        # The description is a little confusing, image[x][y] not really coords point of view
        x, y = y, x
        x_left = firstBad(0, x, 1, True)
        x_right = firstBad(x, n - 1, 0, True)
        y_top = firstBad(0, y, 1, False)
        y_bottom = firstBad(y, m - 1, 0, False)
        return (y_bottom - y_top) * (x_right - x_left)

    # Other approaches
    # 1. DFS on the connected component (Good for large image, bad for large component)
    # 2. Brute force in finding x_left, x_right, y_top, y_bottom (Good for narrow margin)
    # This approach is only on the frame size MlogN + NlogM
    # This question is very open ended. Not good for OJ.