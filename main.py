class SearchEngine:
    def __init__(self):
        self.index = {}

    def add(self, document_id, text):
        text = text.lower()

        words = text.split()

        for word in words:
            if word not in self.index:
                self.index[word] = set()

            self.index[word].add(document_id)