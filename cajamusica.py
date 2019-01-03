import random

PISTAS_FILE = "Pistas.dat"

def load_pistas():
    with open(PISTAS_FILE, 'r', encoding="UTF-8") as f:
        pistas = list(map(lambda p: p.strip(), f.read().splitlines()))
    return pistas

class CajaMusica:
    def __init__(self):
        self.NOTAS = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
        self.pistas = load_pistas()

    def fit(self, word):
        return any(n in word for n in self.NOTAS)

    def get_pista(self):
        return random.sample(self.pistas, 1)[0]
