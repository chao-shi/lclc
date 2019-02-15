class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preq_cnt = collections.defaultdict(int)
        dependon_map = collections.defaultdict(set)
        for a, b in prerequisites:
            preq_cnt[a] += 1
            dependon_map[b].add(a)

        # no need for set, finer controller for insertion
        no_deps = collections.deque()
        no_deps.extend([i for i in range(numCourses) if preq_cnt[i] == 0])
        seq = []
        
        while no_deps:
            for _ in range(len(no_deps)):
                no_dep = no_deps.pop()
                for after in dependon_map.get(no_dep, []):
                    preq_cnt[after] -= 1
                    if preq_cnt[after] == 0:
                        no_deps.append(after)                
                seq.append(no_dep)
        
        return len(seq) == numCourses

# Not strictly BFS here because we pop and append at the same end. 
# Which end does not matter, no_deps is more like a set rather than queue