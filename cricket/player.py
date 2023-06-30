class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience
        self.runs_scored = 0

    def is_out(self):
        # Perform calculations to determine if the player is out
        return False  # Placeholder value
    def add_runs(self, runs):
        self.runs_scored += runs
        