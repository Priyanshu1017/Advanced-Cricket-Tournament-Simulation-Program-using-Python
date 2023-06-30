import random
from cricket.commentator import Commentator

class Teams:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.captain = None
        self.commentator = Commentator(self)
        
    def add_player(self, player):
        self.players.append(player)

    def select_captain(self):
        Cap=self.captain = random.choice(self.players)
        print(f"{self.captain.name} is the captain of {self.name}.")

    def send_next_player(self):
        return random.choice(self.players)

    def choose_bowler(self):
        return random.choice(self.players)