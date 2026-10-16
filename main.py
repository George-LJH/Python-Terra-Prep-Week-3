# main.py
from simple_term_menu import TerminalMenu
import os
import sys


def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")


def run(script):
    os.execv(sys.executable, [sys.executable, script])


def main():
    choice = ""
    while choice != "Quit":
        clearConsole()
        options = ["Slot Machine", "Horse Betting", "Quit"]
        terminal_menu = TerminalMenu(options, title="-- Main Menu --")
        terminalMenu = TerminalMenu(options)
        menuEntryIndex = terminalMenu.show()
        if menuEntryIndex is None:
            break
        choice = options[menuEntryIndex]
        if choice == "Slot Machine":
            run("slotMachine.py")

        if choice == "Horse Betting":
            run("horseBetting.py")


if __name__ == "__main__":
    main()