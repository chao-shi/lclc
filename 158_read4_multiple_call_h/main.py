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
        len_buffered = min(len(self.carryover), n)
        buf[:len_buffered] = self.carryover[:len_buffered]
        self.carryover = self.carryover[len_buffered:]
        
        bytes_read = self.read_easy(buf, len_buffered, n-len_buffered)
        return bytes_read + len_buffered
    
    
    def read_easy(self, buf, offset, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        bytes_read = 0
        while bytes_read < n:
            tmpbuf = [" "] * 4
            nbytes = read4(tmpbuf)
            if nbytes == 0:
                return bytes_read
            
            length = min(n-bytes_read, nbytes)
            buf[offset+bytes_read : offset+bytes_read+length] = tmpbuf[:length]
            bytes_read+=length
                
            # Carry over the remainder
            if length < nbytes:
                self.carryover = tmpbuf[length:nbytes]
        return bytes_read
    
# Line 24 add offset as additional parameter, writing starts at buf[offset:]