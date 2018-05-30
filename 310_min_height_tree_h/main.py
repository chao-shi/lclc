class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # The key idea is to cut leaves layer by layer !!!
        neighbor = {}
        for e in edges:
            neighbor.setdefault(e[0], set()).add(e[1])
            neighbor.setdefault(e[1], set()).add(e[0])
        
        leaves = filter(lambda x:len(neighbor.get(x, set())) <= 1, range(n))
        remain_cnt = n
        
        while remain_cnt > 2:
            new_leaves = []
            for leaf in leaves:
                n = neighbor[leaf].pop()
                neighbor[n].remove(leaf)
                if len(neighbor[n]) == 1:
                    new_leaves.append(n)
            remain_cnt -= len(leaves)
            leaves = new_leaves
        
        return leaves
    
    # Line 14, originally I wrote == 1, leaf by definition should be 0 or 1. Case of only one node
    # Line 22 should be == 1 instead, otherwise duplidate count new_leaves
    # Also I remove the pop loop

    # Entrying the while loop of 17, containing all the leaves with degree of 1 or 0.
    # If any leaf with degree zero, means remain_cnt == 1 (one node), so line 20 will only hit on 1 degree leaf

    # Leaf cropping algorithm
    # First thought was min heap
    # Why this does not work
    # Let's say we pop one leave and after removing this leaf, making one of its neighbors new leaf
    # This new leaf should come after the old leaves. This is hard to guarantee in min heap
    # Plus min heap update value is hard
    # Only decreasing is a little better, needs to implement the bubble up
    # Test case of 1 - 2 - 3 - 4. 