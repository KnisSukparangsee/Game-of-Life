from colorama import Fore
import time

def render(board):
    for _ in range(2 * len(board[0]) + 1):
        print("_", end="")
    print()
    for row in board:
        print("|", end="")
        line = " ".join(" " if int(x) == 0 else Fore.GREEN + "#" for x in row)
        print(line, end="")
        # print()
        print("|")
    for _ in range(2 * len(board[0]) + 1):
        print("‾", end="")
    print()
    time.sleep(0.5)
