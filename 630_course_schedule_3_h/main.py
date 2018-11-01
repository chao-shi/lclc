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
                heapq.heappush(res, -c[0])
            elif res:
                # Replace one course if that course is longer
                max_d = -res[0]
                if c[0] < max_d:
                    # Courses get earlier scheduled
                    heapq.heapreplace(res, -c[0])
                    time += c[0] - max_d
        return len(res)

# Latest Deadline and pop bigger courses