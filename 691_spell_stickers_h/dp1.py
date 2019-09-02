class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        t = len(target)
        mt = [[sys.maxint] * (len(stickers) + 1) for _ in range(1 << t)]
        mt[0] = [0] * (len(stickers) + 1)
        
        masks = [0]
        
        while masks:
            next_masks = set()
            for m in masks:
                for i in range(1, len(stickers) + 1):
                    mm = self.get_mask_after_using_sticker(target, m, stickers[i-1])
                    mt[m][i] = min(mt[mm][i] + 1, mt[m][i-1])
                    #print bin(m), bin(mm), i, mt[m][i]
                
                for next_mask in self.get_next_masks(m, t):
                    next_masks.add(next_mask)
            masks = next_masks
        return mt[(1<<t) - 1][len(stickers)] if mt[(1<<t) - 1][len(stickers)] < sys.maxint else -1

    
    def get_mask_after_using_sticker(self, target, mask, sticker):
        #print "sticker", sticker, "mask", bin(mask)
        cnt = collections.defaultdict(int)
        for ch in sticker:
            cnt[ch] += 1
        for i, ch in enumerate(target):
            if mask & (1 << (len(target) - i - 1)) > 0 and cnt[ch] > 0:
                #print "char", ch
                mask &= ~(1 << len(target) - i - 1)
                cnt[ch] -= 1
        #print "callback mask", bin(mask)
        return mask
            
    def get_next_masks(self, mask, t):
        res = set()
        for i in range(t):
            cand = (1 << i) | mask
            if cand != mask:
                res.add(cand)
        return res

# Enforcing the right DP sequence