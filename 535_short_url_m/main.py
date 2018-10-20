class Codec:
    
    def __init__(self):
        self.key_map = {}

    def gen_key(self):
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = "".join([chars[random.randint(0, 61)] for _ in range(6)])
        return res

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while True:
            key = self.gen_key()
            if key not in self.key_map:
                break
                
        self.key_map[key] = longUrl
        return key
                

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.key_map.get(shortUrl, "")
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


# Implement solution 5.
# Problem of 1, 2 (counter based): an increment pattern
# Problem of 3. hashcode collision 
# Problem of 4, no alphabets, only digits