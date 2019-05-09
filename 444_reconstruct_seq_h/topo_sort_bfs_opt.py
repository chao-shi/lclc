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

        q = collections.deque()
        right_seq = []

        # careful here to use elements as key
        for zero_in in filter(lambda x:len(in_map[x]) ==0, elements):
            q.append(zero_in)

        while q:
            # Detected multiple possible sequence, because of multiple free node with zero in
            if len(q) > 1:
                return False

            zero_in = q.popleft()
            right_seq.append(zero_in)

            for next in out_map.get(zero_in, []):
                in_map[next].remove(zero_in)
                if len(in_map[next]) == 0:
                    q.append(next)

        # Second condition capture the case that
        # Some nodes cannot be visited due to loops
        # Cover both loops under the src and loops in other components
        return right_seq == org and set(right_seq) == elements

# This is clearer than the PQ approach
# It picks one node with zero in-degree and does the topo-sort from there
# Check if all nodes are visited and the topology sort return same as the origin 
# 
# Update not so clean now, still needs to check if any node is zero in-d