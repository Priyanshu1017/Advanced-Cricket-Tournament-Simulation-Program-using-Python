from cricket.team import Teams
from cricket.player import Player
from cricket.match import Match
from cricket.field import Field
import random

def main():
    # Create players for both teams
    player1 = Player("Player 1", 0.2, 0.8, 0.99, 0.8, 0.9)
    player2 = Player("Player 2", 0.3, 0.7, 0.95, 0.7, 0.8)
    player3 = Player("Player 3", 0.1, 0.9, 0.98, 0.9, 0.95)
    player4 = Player("Player 4", 0.3, 0.6, 0.92, 0.6, 0.75)
    player5 = Player("Player 5", 0.4, 0.5, 0.91, 0.5, 0.85)
    player6 = Player("Player 6", 0.25, 0.75, 0.97, 0.75, 0.88)
    player7 = Player("Player 7", 0.35, 0.65, 0.93, 0.65, 0.78)
    player8 = Player("Player 8", 0.15, 0.85, 0.96, 0.85, 0.92)
    player9 = Player("Player 9", 0.35, 0.55, 0.94, 0.55, 0.72)
    player10 = Player("Player 10", 0.45, 0.45, 0.89, 0.45, 0.82)

    # Create teams and add players
    team1 = Teams("Team 1")
    team1.add_player(player1)
    team1.add_player(player2)
    team1.add_player(player3)
    team1.add_player(player4)
    team1.add_player(player5)

    team2 = Teams("Team 2")
    team2.add_player(player6)
    team2.add_player(player7)
    team2.add_player(player8)
    team2.add_player(player9)
    team2.add_player(player10)
    
    # Select captains
    team1.select_captain()
    team2.select_captain()
    
    # Create field and umpire
    field = Field("Large", 0.7, "Dry", 0.1)

    # Create the match
    cricket_match = Match(team1, team2, field)
    cricket_match.start_match()

    # Simulate the match
    cricket_match.simulate_match()
if __name__ == "__main__":
    main()