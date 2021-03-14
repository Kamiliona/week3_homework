from app.models.player import *

player1 = Player("Alaska Thunderfuck","Scissors")
player2 = Player("Sherry the Love", "Rock")
player3 = Player("Bimini Bon Boulash", "Paper")

players = [player1, player2, player3]

def add_new_player(player):
    players.append(player)
