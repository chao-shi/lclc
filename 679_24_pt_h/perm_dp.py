class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def operate(num1, num2, op):
            n1, d1 = num1
            n2, d2 = num2
            if op == "+":
                res = (n1 * d2 + n2 * d1, d1 * d2)
            elif op == "-":
                res = (n1 * d2 - n2 * d1, d1 * d2)
            elif op == "*":
                res = (n1 * n2, d1 * d2)
            elif op == "/":
                res = (n1 * d2, n2 * d1)
            
            n, d = res
            if d == 0:
                return None
            elif n == 0:
                return (n, d)
            else:
                g = gcd(n, d)
                return (n/g, d/g)                

        def gcd(n1, n2):
            n1, n2 = max(n1, n2), min(n1, n2)
            while n1 % n2 != 0:
                n1, n2 = n2, n1 % n2
            return n2
        
        
        def run_perm(nums):
            mt = [[set() for _ in range(5)] for _ in range(5)]

            for i in range(4):
                mt[i][i+1].add((nums[i], 1))


            for diff in range(2, 5):
                for i in range(5 - diff):
                    j = i + diff
                    for k in range(i + 1, j):
                        vs1, vs2 = mt[i][k], mt[k][j]
                        for v in [operate(v1, v2, op) for v1 in vs1 for v2 in vs2 for op in "+-/*"]:
                            if v != None:
                                mt[i][j].add(v)

            return (24, 1) in mt[0][4]
        

        def all_perms(nums):
            perms = [[]]
            for num in nums:
                new_perms = []
                for perm in perms:
                    for i in range(len(perm) + 1):
                        new_perms.append(perm[:i] + [num] + perm[i:])
                perms = new_perms
            return perms
        
        perms = all_perms(nums)
        return any(run_perm(perm) for perm in perms)
        
# Corner case , there will be nominator or denominator being zero, see block 20-26
# Permutation seems annoying, see backtrack.py
