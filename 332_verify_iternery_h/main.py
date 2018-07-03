class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        next_map = {}
        for t in tickets:
            next_map.setdefault(t[0], []).append(t[1])
        
        for src in next_map:
            next_map[src].sort(reverse=True)
        
        res = []
        def recur(city):
            while next_map.get(city, []):
                recur(next_map[city].pop())
            res.append(city)
            
        recur("JFK")
        return res[::-1]

# Euler path.

# A ----- B ------ C -------- D
#        /\
#       /  \
#       E - F

# as example

# We may end up find the path A-B-C-D first, how about the rest the edges still not visited
# We can check that B still have degree non zero, so start constructing path from B
# This is not very efficient because we need to know where B is in the path A-B-C-D

# Instead this information can be stored in the recursion way, that's why when we backtracing to B, we will add 
# B-E-F before B-C-D to form B-E-F-C-D
# That explains why res appending, we are actually doing prepending.
# We prepend when backtrace finishes

# Another thing we need to do is to guarantee dictionary order
# If B has another small loop there, we need to visit smaller letter first.