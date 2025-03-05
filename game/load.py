import numpy as np
import os


def load_file(file):
    array = []
    path = os.path.join("data", file)
    with open(path, "r") as f:
        for line in f:
            chars = []
            for letter in line:
                if letter != "\n":
                    chars.append(letter)
            array.append(chars)
    np_array = np.array(array)
    return np_array
