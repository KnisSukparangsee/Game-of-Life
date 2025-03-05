from colorama import Fore
import time

def render(board):
    print()
    for row in board:
        line = " ".join(" " if int(x) == 0 else Fore.GREEN + "#" for x in row)
        print(line, end="")
        print()
    print()
    time.sleep(0.2)
