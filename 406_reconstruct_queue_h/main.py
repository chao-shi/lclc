class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # or use key = operator.itemgetter(1, 2), but this only all asc or all desc
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
    
# Sort by heigh desc
# So when you are currently p. ALL The taller people are already in queue. You know where to stand

# I was struggling with the idea that insert at the end, then bubbling to the front.
# But there is no need. Where to insert is very deterministic. insert function is better