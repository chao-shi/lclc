class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            b = data[i] & 0xFF
            lo = leading_one(b)
            if lo == 0:
                i += 1
            else:
                if lo > 4 or lo == 1 or i + lo > len(data):
                    return False
                for j in range(i + 1, i + lo):
                    b = data[j] & 0xFF
                    if b & 0xC0 != 0x80:
                        return False
                i += lo
        return True

def leading_one(num):
    mask = 0x80
    cnt = 0
    while mask > 0:
        if mask & num == 0:
            return cnt
        cnt += 1
        mask >>= 1
    return cntx