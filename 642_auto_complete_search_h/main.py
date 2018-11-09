class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.sentences = sentences
        self.times = times
        self.sent_id_map = {s:i for i, s in enumerate(sentences)}
        self.prefix_map = collections.defaultdict(list)

        for s in self.sent_id_map:
            i = self.sent_id_map[s]
            for j in range(1, len(s) + 1):
                prefix = s[:j]
                self.prefix_map[prefix].append(i)
        
        self.typed = ""

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            sent = self.typed
            if self.typed not in self.sent_id_map:
                self.sentences.append(sent)
                self.times.append(1)
                i = len(self.sentences) - 1
                self.sent_id_map[sent] = i
                for j in range(1, len(sent) + 1):
                    prefix = sent[:j]
                    self.prefix_map[prefix].append(i)
                
            else:
                i = self.sent_id_map[sent]
                self.times[i] += 1

            self.typed = ""
            return []

        self.typed = self.typed + c
        ids = self.prefix_map[self.typed]
        ids = sorted(ids, key=lambda i:(-self.times[i], self.sentences[i]))
        return map(lambda i:self.sentences[i], ids[:3])
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)