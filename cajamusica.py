import random

PISTAS_FILE = "Pistas.dat"

def load_pistas():
    with open(PISTAS_FILE, 'r', encoding="UTF-8") as f:
        pistas = list(map(lambda p: p.strip(), f.read().splitlines()))
    return pistas

class CajaMusica:
    def __init__(self):
        self.NOTAS = {'do', 're', 'mi', 'fa', 'sol', 'la', 'si'}
        self.pistas = load_pistas()
        self.players = {}

    def fit(self, word):
        return any(n in word for n in self.NOTAS)

    def get_pista(self):
        return random.sample(self.pistas, 1)[0]

    def add_word_player(self, word, player):
        if player in self.players.keys():
            self.players[player].add(word)
        else:
            self.players[player] = set()
            self.players[player].add(word)

    def remove_player(self, player):
        if player in self.players.keys():
            del self.players[player]

    def player_win(self, player):
        if player in self.players.keys():
            words = set(self.players[player])
            notas = set()
            while words:
                w = words.pop()
                for n in self.NOTAS:
                    if n in w:
                        notas.add(n)
                        break
            return notas == self.NOTAS
        else:
            return False
