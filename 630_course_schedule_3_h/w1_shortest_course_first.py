class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        # Greedy logic. Pick C1 which is shortest duration and also can finish on time
        # Proof: Assume instead picking C2 is leading to optimial solution, where len(C2) > len(C1)
        # Then all cources after C2 can always be accomadated after C1
        heapq.heapify(courses)
        time = 0
        cnt = 0
        while courses:
            short_d, deadline = heapq.heappop(courses)
            if time + short_d <= deadline:
                time += short_d
                cnt += 1
        return cnt

# Wrong, does not pass
#
# Input:
# [[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]
# Output:
# 4
# Expected:
# 5