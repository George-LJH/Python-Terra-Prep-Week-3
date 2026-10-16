
import pandas as pd
from simple_term_menu import TerminalMenu
import json
import os
import sys
import time
import random
from pathlib import Path
import pyinputplus as pyip
from main import *

        
def gameOver():
    filePath = Path("data.json")
    filePath.unlink(missing_ok=True)
    restartProgram()


def restartProgram():
    print("Restarting script...")
    sys.stdout.flush()
    os.execv(sys.executable, [sys.executable] + sys.argv)

def addData(key, amount=1):
    if key not in data:
        raise KeyError(f"'{key}' is not in the JSON data")
    if not isinstance(data[key], (int, float)):
        raise TypeError(f"'{key}' must contain a number")
    data[key] += amount
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)
    return data[key]
def updateScreen():
    global money
    money = data["money"]

    if money <= 0:
            print("Game Over... You have run out of money. Game Restarted")
            time.sleep(1.5)
            clearConsole()
            gameOver()
    else:
        print(f"Money: {money}")
def startRace():
    print("Starting race...")
    horse1 = random.randint(1, 10)
    horse2 = random.randint(1, 10)
    horse3 = random.randint(1, 10)
    horses = [horse1, horse2, horse3]
    winningHorse = max(horses)
    winningHorseIndex = horses.index(winningHorse)
    return winningHorseIndex + 1
clearConsole()



try:
    with open("data.json", "r") as f:
        data = json.load(f)
        money = data["money"]
        choice = ""
        while choice != "Quit":
            updateScreen()
            options = ["Start Race", "Quit"]
            terminalMenu = TerminalMenu(options)
            menuEntryIndex = terminalMenu.show()
            if menuEntryIndex is None:
                break
            choice = options[menuEntryIndex]
            if choice == "Start Race":
                Chosenhorse = pyip.inputInt("Choose a horse (1, 2, or 3): ", min=1, max=3)
                betAmount = pyip.inputInt("Enter your bet amount: ", min=1, max=money)
                winningHorse = startRace()
                if Chosenhorse == winningHorse:
                    print(f"You won! The winning horse was {winningHorse}.")
                    winnings = betAmount * 2
                    addData("money", winnings)
                else:
                    print(f"You lost! The winning horse was {winningHorse}.")
                    addData("money", -betAmount)
        run("main.py")
except (FileNotFoundError, json.JSONDecodeError):
    print("JSON file does not exist or could not be read. Initializing defaults...")
    data = {"money": 500, "Jackpot777": 0, "Jackpot": 0, "Pairs": 0, "Sequences": 0, "Losses": 0, "Streak": 1} 
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)
    restartProgram()