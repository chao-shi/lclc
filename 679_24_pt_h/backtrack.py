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
        

        def recur(nums):
            if len(nums) == 1:
                return nums[0] == (24, 1)
            
            dup_nums = list(nums)

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    # Multiple pop is wrong
                    # dup_nums = list(nums)
                    # dup_nums.pop(i)
                    # dup_nums.pop(j)
                    
                    dup_nums = [nums[ii] for ii in range(len(nums)) if ii != i and ii != j]

                    for op in "+-/*":
                        val = operate(nums[i], nums[j], op)
                        if val != None:
                            dup_nums.append(val)
                            if recur(dup_nums):
                                return True
                            else:
                                dup_nums.pop()
            return False
        
        return recur(map(lambda x:(x, 1), nums))
                        
            
            
        
# Corner case , there will be nominator or denominator being zero, see block 20-26
# recur try to pick two numbers out of the nums and put back the result of the operator

# Special backtracking, pick out two cands and put in another one

# Careful on line 46 of popping multiple commands is wrong, j is no longer the same after i is popped.