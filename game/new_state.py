from .state import dead_state


def next_board_state(board):
    width, height = len(board[0]), len(board)
    new_state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            living_cells = neighbors(i, j, board)
            if int(board[i][j]) == 0:
                if living_cells == 3:
                    new_state[i][j] = 1
            else:
                if living_cells <= 1 or living_cells > 3:
                    new_state[i][j] = 0
                else:
                    new_state[i][j] = 1
    return new_state


def neighbors(row, col, board):
    rows = len(board)
    cols = len(board[0])
    cells = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i == row and j == col) or i < 0 or j < 0 or i >= rows or j >= cols:
                continue

            if int(board[i][j]) == 1:
                cells += 1
    return cells
