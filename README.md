# Python Games

A collection of games written in Python.

## Projects

- [Slot Machine](#slot-machine)

## Requirements

- Python 3.10 or newer
- The packages listed in `requirements.txt`

## Setup

Install the libraries

```bash
pip install -r requirements.txt
```

## Slot Machine

A terminal-based slot machine with three reels, customizable bets, streaks,
payouts, statistics, and saved progress.

### Run

Start the main menu:

```bash
python3 main.py
```

Use the arrow keys to select **Slot Machine**, then press Enter.

### Features

- Spin three reels.
- Change the bet amount.
- Buy streaks to increase payouts.
- View payouts and statistics.
- Reset the game.
- Save progress in `data.json`.
- Restart with starting money when game over.

### Payouts

Payouts are multiplied by the current streak:

| Result | Base payout |
| --- | ---: |
| Three 7s | 1,000 coins |
| Three matching symbols | 400 coins |
| Three-number sequence | 200 coins |
| Any matching pair | 25 coins |

The game starts with 500 coins and a streak of 1.

## Future Projects

Add each new game as its own top-level section in this README. Include a short
description, run command, features, and any project-specific instructions.
