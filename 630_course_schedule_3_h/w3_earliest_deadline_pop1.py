class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses = sorted(courses, key=lambda x:(x[1], x[0]))
        time = 0
        res = []
        for i, c in enumerate(courses):
            if time + c[0] <= c[1]:
                time += c[0]
                res.append(c)
            elif res and c[0] < res[-1][0]:
                time -= res[-1][0] - c[0]
                res[-1] = c
        return len(res)

# Earliest Deadline
# Wrong, does not pass
# Input:
# [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
# Output:
# 3
# Expected:
# 4