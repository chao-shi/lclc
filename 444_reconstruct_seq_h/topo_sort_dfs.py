import collections
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        in_map, out_map = collections.defaultdict(set), collections.defaultdict(set)
        elements = set()
        for seq in seqs:
            for e in seq:
                elements.add(e)
            for i in range(1, len(seq)):
                in_map[seq[i]].add(seq[i-1])
            for i in range(len(seq) - 1):
                out_map[seq[i]].add(seq[i+1])
                
        # find one with no in_degree
        src = filter(lambda x:len(in_map[x]) ==0, elements)
        
        if len(src) != 1:
            return False

        src = src[0]
        visited = {}
        rev_seq = []
        
        def topo_sort(cur):
            if visited.get(cur, 0) == 1:
                return False
            elif visited.get(cur, 0) == 2:
                return True

            # Some pre-checking
            zero_child_cnt = 0
            for next in out_map.get(cur, []):
                in_map[next].remove(cur)
                if len(in_map[next]) == 0:
                    zero_child_cnt += 1
            if zero_child_cnt > 1:
                return False

            visited[cur] = 1
            for next in out_map.get(cur, []):
                if not topo_sort(next):
                    return False

            visited[cur] = 2
            rev_seq.append(cur)
            return True

        # Not a unique sequence or there is a loop
        if not topo_sort(src):
            return False
        
        # case where the component of src is good, but another component is a loop.
        if len(visited) != len(elements):
            return False
        
        return rev_seq[::-1] == org

# This is clearer than the PQ approach
# It picks one node with zero in-degree and does the topo-sort from there
# Check if all nodes are visited and the topology sort return same as the origin 
# 
# Update not so clean now, still needs to check if any node is zero in-d