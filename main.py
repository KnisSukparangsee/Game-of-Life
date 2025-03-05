from game.state import dead_state, add_state, random_state
from game.new_state import next_board_state
from colorama import init
from game.ui import render
import sys

WIDTH = 60
HEIGHT = 40

def main():
    init(autoreset=True)
    pattern = f"{sys.argv[1]}.txt"
    if (sys.argv[1] == "random"):
        state1 = random_state(WIDTH, HEIGHT)
    else:
        x, y = int(sys.argv[2]), int(sys.argv[3])
        state1 = dead_state(WIDTH, HEIGHT)
        state1 = add_state(x, y, pattern, state1)
    while True:
        render(state1)
        state1 = next_board_state(state1)

        
if __name__ == "__main__":
    main()