import numpy as np
from game.load import load_file


def dead_state(width, height):
    array = np.zeros((height, width))
    return array


def random_state(width, height):
    rng = np.random.default_rng()
    array = rng.integers(2, size=(height, width))
    print(array)
    return array


def add_state(x1, y1, file, array):
    height = len(array)
    width = len(array[0])
    soup = load_file(file)
    x2 = x1 + len(soup[0])
    y2 = y1 + len(soup)
    if y1 + len(soup) < height and x1 + len(soup[0]) < width:
        for i in range(y1, y2):
            for j in range(x1, x2):
                array[i][j] = soup[i - y1][j - x1]
    else:
        print("Soup is out of bounds")
        raise Exception()
    return array
