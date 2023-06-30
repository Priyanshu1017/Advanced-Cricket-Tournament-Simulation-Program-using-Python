# Cricket Match Simulation

This is a Python program that simulates a cricket match between two teams. The program uses classes and objects to model players, teams, field conditions, umpires, and commentators to provide a realistic simulation of a cricket match.

## Features

- The program allows you to create teams with players and assign a captain to each team.
- You can select batsmen and bowlers for each team based on their abilities.
- The program considers field conditions, player skills, and randomness to predict ball outcomes.
- Umpires keep track of the score, wickets, and overs during the match.
- Commentators provide commentary on various game events.
- The match is simulated over a fixed number of overs (currently set to 5 overs for simplicity).

## Structure

The code is organized into several classes:

- `Player`: Represents a cricket player with attributes for name, bowling, batting, fielding, running, and experience.
- `Team`: Represents a cricket team with attributes for name, players, captain, batsmen, and bowlers.
- `Field`: Represents the cricket field with attributes for size, fan ratio, pitch conditions, and home advantage.
- `Umpire`: Represents the umpire in the match with attributes for score, wickets, and overs. It also provides methods for predicting ball outcomes and handling events.
- `Commentator`: Represents the commentator who provides commentary during the match.
- `Match`: Represents the cricket match with attributes for the two teams, field, umpire, and commentator. It provides a method to simulate the match.

## Usage

1. Ensure you have Python installed on your system.
2. Clone or download the code from this repository.
3. Open a terminal or command prompt and navigate to the directory containing the code files.
4. Run the `main.py` file using the command: `python main.py`.
5. The simulation will start, and you will see the commentary and final score.

Feel free to modify the player attributes, team compositions, field conditions, or match settings to customize the simulation according to your requirements.

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
