# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.carryover = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        bytes_read = 0
        while bytes_read < n:
            if self.carryover:
                tmpbuf = self.carryover
                nbytes = len(tmpbuf)
            else:
                tmpbuf = [" "] * 4
                nbytes = read4(tmpbuf)

            if nbytes == 0:
                return bytes_read
            
            i = 0
            length = min(n-bytes_read, nbytes)
            buf[bytes_read:bytes_read+length] = tmpbuf[:length]
            bytes_read+=length
            
            # if consumed < read, there is carryover
            self.carryover = tmpbuf[length:nbytes]

        return bytes_read