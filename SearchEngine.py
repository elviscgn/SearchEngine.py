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

    def search(self, search_word):
        search_word = search_word.lower()

        if search_word in self.index:
            return sorted(self.index[search_word])

        return []
    
engine = SearchEngine()

engine.add(1, "Explore the hidden trails in the Drakensberg mountains")
engine.add(2, "Join us for a weekend braai in Johannesburg with friends")
engine.add(3, "Discover Table Mountain and the beaches of Cape Town")
engine.add(4, "Listen to Kwaito and Afrobeat music on SA Radio")
engine.add(5, "Braais and live music make Durban weekends special")
