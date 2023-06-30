
class Commentator:
    def __init__(self, match):
        self.match = match
        

    def provide_commentary(self, ball, over):
        batsman = ball["batsman"]
        bowler_name = ball["bowler"]
        runs_scored = ball["runs"]
        is_out = ball["is_out"]
        toss_winner = ball["toss_winner"]  # Get toss winner from the ball dictionary
        toss_decision = ball["toss_decision"]  # Get toss decision from the ball dictionary
        commentary = ""
        
        if batsman is not None:
            batsman_name = batsman.name
            bowler_name = bowler_name.name
            commentary += f"{batsman_name} facing {bowler_name}. "

        if is_out:
            commentary += f"Oh no! {batsman_name} is out!"
        else:
            if runs_scored == 0:
                commentary += "Dot ball. nice bowling!"
            elif runs_scored == 4:
                commentary += "FOUR runs!  Fantastic shot!"
            elif runs_scored == 6:
                commentary += "SIX runs! terrific shot!"
            else:
                commentary += f"{runs_scored} runs scored."

        if over % 6 == 0:
            commentary += f"\n End of over {over}."
        if over == 0:
            print(f"Welcome to the match between {self.match.team1.name} and {self.match.team2.name}.")
            commentary += f"\n {toss_winner} won the toss and choose to {toss_decision} first."  # Include toss information in the commentary

        print("\n",commentary)


    def announce_match_result(self, team1_runs, team2_runs):
        print("\n  ------------------------------------")
        print(f"{self.match.team1.name} scored {team1_runs} runs.")
        print(f"{self.match.team2.name} scored {team2_runs} runs.")
        print("\n ------------------------------------")
        if team1_runs > team2_runs:
            print(f"{self.match.team1.name} won by {team1_runs - team2_runs} runs.")
        elif team2_runs > team1_runs:
            print(f"{self.match.team2.name} won by {team2_runs - team1_runs} runs.")
        else:
            print("Match tied.")