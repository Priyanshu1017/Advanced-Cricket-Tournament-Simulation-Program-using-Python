import random
from cricket.commentator import Commentator

class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.current_batting_team = None
        self.current_bowling_team = None
        self.innings = 1
        self.commentator = Commentator(self)

    def start_match(self):
        # Select the captain of both teams randomly
        self.team1.captain
        self.team2.captain

        # Perform toss and decide batting or bowling randomly for the toss winner
        toss_winner = random.choice([self.team1, self.team2])
        toss_decision = random.choice(["bat", "bowl"])

        if toss_decision == "bat":
            self.current_batting_team = toss_winner
            self.current_bowling_team = (
                self.team2 if toss_winner == self.team1 else self.team1
            )
        else:
            self.current_batting_team = (
                self.team2 if toss_winner == self.team1 else self.team1
            )
            self.current_bowling_team = toss_winner

        # Provide toss information to the commentator
        toss_info = {
            "batsman": None,  # Set batsman to None for toss information
            "bowler": None,  # Set bowler to None for toss information
            "runs": None,  # Set runs to None for toss information
            "is_out": False,
            "toss_winner": toss_winner.name,  # Add toss winner to the toss information
            "toss_decision": toss_decision,  # Set is_out to False for toss information
        }
        self.commentator.provide_commentary(toss_info, 0)

    def change_innings(self):
        self.innings += 1
        self.current_batting_team, self.current_bowling_team = (
            self.current_bowling_team,
            self.current_batting_team,
        )

    def simulate_match(self):
        # Batting innings
        current_batsman = self.current_batting_team.send_next_player()
        current_bowler = self.current_bowling_team.choose_bowler()
        over = 1

        while self.innings <= 2:
            ball = {
            "batsman": current_batsman,
            "bowler": current_bowler,
            "runs": random.choice([0, 1, 2, 3, 4, 6]),
            "is_out": current_batsman.is_out(),
            "toss_winner": self.current_batting_team.name,  # Pass toss winner explicitly
            "toss_decision": "bat" if self.current_batting_team == self.team1 else "bowl",  # Pass toss decision explicitly
        }

            is_out = ball["is_out"]
            current_batsman.add_runs(ball["runs"])  # Update runs scored by the batsman

            self.commentator.provide_commentary(ball,over)

            if is_out:
                current_batsman = self.current_batting_team.send_next_player()

                ball[
                    "batsman"
                ] = current_batsman  # Update the batsman in the ball dictionary

            if over % 6 == 0:
                if self.innings == 1 and len(self.current_batting_team.players) == len(
                    self.team1.players
                ):
                    self.change_innings()
                elif self.innings == 2 and len(
                    self.current_batting_team.players
                ) == len(self.team2.players):
                    self.change_innings()

            current_batsman = self.current_batting_team.send_next_player()
            current_bowler = self.current_bowling_team.choose_bowler()
            over += 1

        # Calculate total runs of each team
        team1_runs = sum(player.runs_scored for player in self.team1.players)
        team2_runs = sum(player.runs_scored for player in self.team2.players)

        self.commentator.announce_match_result(team1_runs, team2_runs)
