import collections
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # Find nexts should skip all the equal ones starting at i
        def find_nexts(S, i):
            while i < len(S) and S[i] == B[i]:
                i += 1
            res = []
            for j in range(i + 1, len(S)):
                if S[j] == B[i]:
                    SS = S[:i] + S[j] + S[i+1:j] + S[i] + S[j+1:]
                    res.append((SS, i + 1))
            return res

        q = collections.deque([(A, 0)])
        visited = set([(A, 0)])
        steps = 0

        while q:
            for _ in range(len(q)):
                S, i = q.popleft()
                if S == B:
                    return steps
                for n in find_nexts(S, i):
                    if n not in visited:
                        q.append(n)
                        visited.add(n)
            steps += 1