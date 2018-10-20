class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, ai = map(int, a[:len(a)-1].split("+"))
        br, bi = map(int, b[:len(b)-1].split("+"))
        r = ar * br - ai * bi
        i = ar * bi + br * ai
        return "{}+{}i".format(r, i)