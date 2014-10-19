from itertools import permutations
from helpers import helpers

MATRIX_WIDTH = 1001
SPIRAL_DEPTH = int(MATRIX_WIDTH/2)

def main():
    diagonals = []

    i = 1
    diagonals.append(i)
    for depth in range(1, SPIRAL_DEPTH + 1):
        # For each edge of the current "circle"
        for _ in range(4):
            # Jump the gap between the corners
            i += 2 * depth

            # Store the corner
            diagonals.append(i)

    answer = sum(diagonals)
    print(answer)


if __name__ == '__main__':
    main()
