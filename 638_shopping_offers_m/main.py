class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        mt = {}

        def recur(remains, i):
            if all(r == 0 for r in remains):
                return 0
            elif i == 0:
                return sum(remains[ii] * price[ii] for ii in range(len(remains)))
            elif (remains, i) in mt:
                return mt[(remains, i)]
            else:
                minv = recur(remains, i - 1)
                sp = special[i-1]
                new_remains = [remains[ii] - sp[ii]  for ii in range(len(remains))]
                
                if all(r >= 0 for r in new_remains):
                    minv = min(minv, recur(tuple(new_remains), i) + sp[-1])
                    
                mt[(remains, i)] = minv
                return minv
            
        return recur(tuple(needs), len(special))
        
            