# keyword_spotting.py

class KeywordSpotting:
    def __init__(self, keywords):
        self.keywords = keywords

    def spot_keywords(self, sentence):
        spotted = [word for word in self.keywords if word in sentence]
        return spotted
