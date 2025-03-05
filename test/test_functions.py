from game.load import load_file
from game.new_state import next_board_state
from game.new_state import neighbors
import pytest
import numpy as np


@pytest.fixture
def dead_state():
    return np.zeros((3, 3))

    
@pytest.fixture
def living_state():
    return np.ones((3, 3))


def test_next_board_state_dead(dead_state):
    expected_state = np.zeros((3,3))
    actual_state = next_board_state(dead_state)
    assert (actual_state == expected_state).all()

    # Reproduce cell when 3 living cells neighbor 1 dead cell
    initial_state = np.array([[0,1,0],[1,1,0],[0,0,0]])
    actual_state = next_board_state(initial_state)
    expected_state = np.array([[1,1,0],[1,1,0],[0,0,0]])
    assert (actual_state == expected_state).all()


def test_next_board_state_alive(living_state, dead_state):
    # Overpopulation death when there are more than 3 living cells nearby
    expected_state = np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
    actual_state = next_board_state(living_state)
    assert (actual_state == expected_state).all()

    # Underpopulation death when there are 0 or 1 living cells nearby
    initial_state = np.array([[0,1,0],[0,0,0],[0,1,0]])
    actual_state = next_board_state(initial_state)
    expected_state = dead_state
    assert (actual_state == expected_state).all()

    # Survival when there are 2 or 3 living cells nearby
    initial_state = np.array([[1,1,0],[1,0,1],[0,1,1]])
    actual_state = next_board_state(initial_state)
    expected_state = np.array([[1,1,0],[1,0,1],[0,1,1]])
    assert (actual_state == expected_state).all()


def test_next_board_state_toad():
    actual_state = next_board_state(load_file("toad.txt"))
    expected_state = np.array([[0,0,0,0,0,0],[0,0,0,1,0,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,0,1,0,0,0],[0,0,0,0,0,0]])
    assert (actual_state == expected_state).all()


@pytest.mark.parametrize("row, col", [(0, 0), (2, 0), (0, 2), (2, 2)])
def test_neighbors_corners(row, col, dead_state, living_state):
    living_cells = neighbors(row,col,living_state)
    dead_cells = neighbors(row,col,dead_state)
    assert living_cells == 3
    assert dead_cells == 0


@pytest.mark.parametrize("row, col", [(0, 1), (1, 0), (2, 1), (1, 2)])
def test_neighbors_edges(row, col, living_state, dead_state):
    living_cells = neighbors(row, col, living_state)
    dead_cells = neighbors(row, col, dead_state)
    assert living_cells == 5
    assert dead_cells == 0
