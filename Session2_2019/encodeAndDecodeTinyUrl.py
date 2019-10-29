class Codec:
    def __init__(self):
        self.valids = string.ascii_letters + '0123456789'
        self.urlCode = {}
        self.codeUrl = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.urlCode:
            code = ''.join([random.choice(self.valids) for _ in range(0,6)])
            if code not in self.codeUrl:
                self.codeUrl[code] = longUrl
                self.urlCode[longUrl] = code
        return 'http://tinyurl.com/' + self.urlCode[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        shortUrl = shortUrl[-6:]
        return self.codeUrl[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
