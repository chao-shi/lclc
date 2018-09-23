class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def validate_v4(IP):
            segs = IP.split(".")
            if len(segs) != 4:
                return False
            for seg in segs:
                if not seg:
                    return False
                # Need test int()
                elif any(not ch.isdigit() for ch in seg):
                    return False
                elif int(seg) < 0 or int(seg) > 255:
                    return False
                elif str(int(seg)) != seg:
                    # leading zeros
                    return False
            return True
        
        
        def validate_v6(IP):
            segs = IP.split(":")
            if len(segs) != 8:
                return False
            
            for seg in segs:
                if not seg or len(seg) > 4:
                    return False
                elif any(not ch.isdigit() and ch not in "ABCEDFabcdef" for ch in seg):
                    return False
            return True
        
        if validate_v4(IP):
            return "IPv4"
        elif validate_v6(IP):
            return "IPv6"
        else:
            return "Neither"
            
            
# How to follow up and handle :: case
# First we need to make sure that there are is only one ::
# Two of them is ambigous. Then we can fill the segs with all zeros
# and pass to another function
                    