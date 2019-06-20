import collections
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        def get_next(i, avail):
            return [j for j in avail if B[j] == A[i]]

        def find_component(src, avail):
            q = collections.deque()
            q.append(src)
            path_map = {src: [src]}
            while q:
                i = q.popleft()
                path_i = path_map[i]
                for n in get_next(i, avail):
                    # find a loop
                    if n == src:
                        return path_i
                    elif n not in path_map:
                        q.append(n)
                        path_map[n] = path_i + [n]

        ans = 0
        avail = set(range(len(A)))
        for i in range(len(A)):
            if i in avail:
                comp = find_component(i, avail)
                print comp, [A[ii] for ii in comp]
                for e in comp:
                    avail.remove(e)
                ans += len(comp) - 1
        return ans

print Solution().kSimilarity("aabbccddee", "cdacbeebad")

# Key idea is to find the minimal components where each pair has to be swapped.
# 
# Does not pass 
# 
# Reason is that when finding the min component for first element, there may be multiple options,
# some options may occupy others so that the total may not be optimal.