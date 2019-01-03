from nltk.corpus import wordnet

class Dictionary:
    def __init__(self):
        pass

    def synonyms(self, word):
        synonyms = set()
        synset_clases = wordnet.synsets(word, lang='spa')
        for ss in synset_clases:
            lemmas = ss.lemma_names('spa')
            for s in lemmas:
                synonyms.add(s)
        return synonyms

    def antonyms(self, word):
        word = word.lower()
        pass
