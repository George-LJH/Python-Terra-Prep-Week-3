# main.py
from simple_term_menu import TerminalMenu
import os
import sys


def clearConsole():
    os.system("cls" if os.name == "nt" else "clear")


def run(script):
    os.execv(sys.executable, [sys.executable, script])


def main():
    clearConsole()
    options = ["Slot Machine", "Quit"]
    terminal_menu = TerminalMenu(options, title="-- Main Menu --")
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        run("slotMachine.py")


if __name__ == "__main__":
    main()