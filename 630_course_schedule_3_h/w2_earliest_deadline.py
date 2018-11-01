class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses = sorted(courses, key=lambda x:(x[1], x[0]))
        time = 0
        cnt = 0
        for i, c in enumerate(courses):
            if time + c[0] <= c[1]:
                time += c[0]
                cnt += 1
        return cnt

# Wrong, does not pass
# Input:
# [[5,5],[4,6],[2,6]]
# Output:
# 1
# Expected:
# 2