

class CajaMusica:
    def __init__(self):
        self.NOTAS = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']

    def fit(self, word):
        word = word.lower()
        return any(n in word for n in self.NOTAS)
