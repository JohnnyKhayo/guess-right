# Guess Right

A simple yet polished command-line number guessing game. Choose a difficulty, try to guess the secret number, get helpful hints, and compete on a local leaderboard.

## Features

- Three difficulty levels (Easy, Medium, Hard)
- Smart input validation
- Hints after three wrong guesses
- High score saving
- Leaderboard with optional difficulty filter
- Option to play multiple rounds

## Requirements

- Python 3.8 or higher

No external packages are required. The game uses only the Python standard library.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/guess-right.git
   cd guess-right
   ```

2. (Recommended) Create and activate a virtual environment:
   bash

```
python -m venv venv
```

### . Windows (PowerShell):
powershell
```
.\venv\Scripts\Activate.ps1
```

### . Windows (Git Bash) / macOS / Linux:
```
bash

source venv/bin/activate
```

## How to Run

```bash

python main.py
```

## How to Play
1. Choose a difficulty level.
2. Guess a number between 1 and 100.
3. Use the feedback (“Too Low” / “Too High”) and hints to find the number.
4. After a successful game you can save your score.
5. View the leaderboard at any time.
6. Play again or exit.

## Difficulty Levels
Level
Attempts
Easy
10
Medium
7
Hard
5

## Hints
After three incorrect guesses the game gives you one or more of the following hints:
. Whether the number is even or odd
. Whether the number is divisible by 5

## Project Structure

```
guess-right/
├── main.py
├── .gitignore
├── README.md
├── LICENSE
└── high_scores.txt   # created automatically when a score is saved
```

## High Scores

Scores are stored locally in high_scores.txt. This file is ignored by Git so each player keeps their own scores.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

````
You can copy this directly into your `README.md`.  
Would you like any section adjusted (for example, adding your real GitHub username or a short “Contributing” section)?
````


