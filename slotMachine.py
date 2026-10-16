
from simple_term_menu import TerminalMenu
import json
import os
import sys
import time
import random
from pathlib import Path
import pyinputplus as pyip
betAmount = 1


def spin():
    if money >= betAmount:
        addData("money", -betAmount)
        full = [random.randint(1, 7), random.randint(1, 7), random.randint(1, 7)]
        for i in range(10):
            time.sleep(0.1)
            clearConsole()
            print(random.randint(1, 7), random.randint(1, 7), random.randint(1, 7))
        clearConsole()
        return full
    else:
        print("Not enough money to spin.")
        time.sleep(1)
    

        
def gameOver():

    file_path = Path("data.json")
    file_path.unlink(missing_ok=True)
    restartProgram()
def checkWin(numbers):
    global money, jackpot777, jackpot, pairs, sequences, losses, streak
    num1 = numbers[0]
    num2 = numbers[1]
    num3 = numbers[2]
    is_sequence = (num1 + 1 == num2 and num2 + 1 == num3) or (num3 - 1 == num2 and num2 - 1 == num1)
    is_win = num1 == num2 == num3 or num1 == num2 or num1 == num3 or num2 == num3 or is_sequence
    if is_win:
        green = "\033[42m\033[30m"
        reset = "\033[0m"
        if num1 == num2 == num3 or is_sequence:
            winning_positions = {0, 1, 2}
        elif num1 == num2:
            winning_positions = {0, 1}
        elif num1 == num3:
            winning_positions = {0, 2}
        else:
            winning_positions = {1, 2}

        result = []
        for index, number in enumerate(numbers):
            if index in winning_positions:
                result.append(f"{green}{number}{reset}")
            else:
                result.append(str(number))
        print(*result)
    else:
        print(num1, num2, num3)
    if num1 == num2 == num3:
        if num1 == 7:
            print(f"777 Jackpot! You win {1000 * streak} coins!")
            addData("money", 1000 * streak)
            addData("Jackpot777", 1)
        else:
            print(f"Jackpot! You win {400 * streak} coins!")
            addData("money", 400 * streak)
            addData("Jackpot", 1)
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print(f"Pairs! You win {25 * streak} coins!")
        addData("money", 25 * streak)
        addData("Pairs", 1)
    elif is_sequence:
        print(f"Sequences! You win {200 * streak} coins!")
        addData("money", 200 * streak)
        addData("Sequences", 1)
    else:
        print("You lose!")
        addData("Losses", 1)
    money = data["money"]
    jackpot777 = data["Jackpot777"]
    jackpot = data["Jackpot"]
    pairs = data["Pairs"]
    sequences = data["Sequences"]
    losses = data["Losses"]
    streak = data["Streak"]
def restartProgram():
    print("Restarting script...")
    sys.stdout.flush()
    os.execv(sys.executable, [sys.executable] + sys.argv)
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    global money, jackpot777, jackpot, pairs, sequences, losses, streak
    money = data["money"]
    jackpot777 = data["Jackpot777"]
    jackpot = data["Jackpot"]
    pairs = data["Pairs"]
    sequences = data["Sequences"]
    losses = data["Losses"]
    streak = data["Streak"]
    clearConsole()
    
    if money <= 0:
        
            print("Game Over... You have run out of money. Game Restarted")
            time.sleep(1.5)
            clearConsole()
            gameOver()
    else:
        print(f"Money: {money} | 777 Jackpot: {jackpot777} | Jackpot: {jackpot} | Pairs: {pairs} | Sequences: {sequences} | Losses: {losses} | Streak: {streak}")
clearConsole()



try:
    with open("data.json", "r") as f:
        data = json.load(f)
    if "money" in data and "Jackpot777" in data and "Jackpot" in data and "Pairs" in data and "Sequences" in data and "Losses" in data and "Streak" in data:
        money = data["money"]
        jackpot777 = data["Jackpot777"]
        jackpot = data["Jackpot"]
        pairs = data["Pairs"]
        sequences = data["Sequences"]
        losses = data["Losses"]
        streak = data["Streak"]
        choice = ""
        updateScreen()
        while choice != "Quit":
            
            updateScreen()
            options = ["Spin", "Buy Streak", "View Payout", "View Stats", "Reset Game", "Change Bet Amount", "Quit"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            choice = options[menu_entry_index]
            if choice == "Spin":
                numbers = spin()
                if numbers is not None:
                    checkWin(numbers)
                # print(money, jackpot777, jackpot, pairs, sequences, losses, streak)
                time.sleep(1)
                clearConsole()
                updateScreen()
            elif choice == "Buy Streak":
                cost = 20
                maximum_amount = money // cost
                if maximum_amount >= 1:
                    amount = pyip.inputInt(
                        prompt=f"How many streaks do you want to buy? (1 to {maximum_amount}): ",
                        min=1,
                        max=maximum_amount,
                    )
                    total_cost = cost * amount
                    addData("money", -total_cost)
                    addData("Streak", amount)
                    updateScreen()
                else:
                    print("Not enough money to buy that many streaks.")
            elif choice == "View Payout":
                clearConsole()
                print("Payouts:")
                print(f"777 Jackpot: {1000 * streak} coins")
                print(f"Jackpot: {400 * streak} coins")
                print(f"Sequences: {200 * streak} coins")
                print(f"Pairs: {25 * streak} coins")
                input("Press ENTER to continue...")
            elif choice == "View Stats":
                clearConsole()
                print("Stats:")
                print(f"777 Jackpot: {jackpot777}")
                print(f"Jackpot: {jackpot}")
                print(f"Sequences: {sequences}")
                print(f"Pairs: {pairs}")
                print(f"Losses: {losses}")
                input("Press ENTER to continue...")
            elif choice == "Reset Game":
                confirm = input("Are you sure you want to reset the game? This will delete your data. (y/n): ")
                if confirm.lower() == "y":
                    file_path = Path("data.json")
                    file_path.unlink(missing_ok=True)
                    restartProgram()
                else:
                    print("Reset cancelled.")
            elif choice == "Change Bet Amount":
                newBet = pyip.inputInt(prompt=f'Enter a number (1 to {money}): ', min=1, max=money)
                if newBet > 0:
                    betAmount = newBet
                    print(f"Bet amount changed to {betAmount}.")
                else:
                    print("Invalid bet amount. Must be greater than 0.")

    else:
        print("JSON file missing data. Setting defaults...")
        data.setdefault("money", 500)
        data.setdefault("Jackpot777", 0)
        data.setdefault("Jackpot", 0)
        data.setdefault("Pairs", 0)
        data.setdefault("Sequences", 0)
        data.setdefault("Losses", 0)
        data.setdefault("Streak", 1)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=2)
        restartProgram()
except (FileNotFoundError, json.JSONDecodeError):
    print("JSON file does not exist or could not be read. Initializing defaults...")
    data = {"money": 500, "Jackpot777": 0, "Jackpot": 0, "Pairs": 0, "Sequences": 0, "Losses": 0, "Streak": 1} 
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)
    restartProgram()



