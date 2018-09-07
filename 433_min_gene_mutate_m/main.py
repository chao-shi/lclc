class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        
        def mutate_one(gene):
            ret = []
            for i in range(len(gene)):
                for ch in "ACGT":
                    gene_next = gene[:i] + ch + gene[i+1:]
                    if gene_next != gene and gene_next in bank:
                        ret.append(gene_next)
            return ret
        
        level = [start]
        level_cnt = 0

        while level:
            if end in level:
                return level_cnt
            next_level = []
            for g in level:
                for gg in mutate_one(g):
                    next_level.append(gg)
                    bank.remove(gg)
            level = next_level
            level_cnt += 1
        
        return -1        

# How to only use bank to avoid revisiting the same.