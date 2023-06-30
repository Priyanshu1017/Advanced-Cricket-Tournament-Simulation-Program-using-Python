class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage
        
        print(f"Field size: {self.size}")
        print(f"Fan ratio: {self.fan_ratio}")
        print(f"Pitch conditions: {self.pitch_conditions}")
        print(f"Home advantage: {self.home_advantage}")