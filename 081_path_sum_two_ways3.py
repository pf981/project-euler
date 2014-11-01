import numpy as np

def iterate_zigzag(matrix):
    """
    Iterates over the matrix in the following order
    17 15 13 10
    14 12 9  6
    11 8  5  3
    7  4  2  1
    """
    # In the docstring example, this iterates through 1 to 10
    for start_column in reversed(range(len(matrix))):
        for row in reversed(range(start_column + 1, len(matrix))):
            yield (row, len(matrix) + start_column - row)

    # In the docstring example, this iterates through 11 to 17
    for start_row in reversed(range(len(matrix))):
        for column in range(start_row + 1):
            yield (start_row - column, column)


def min_of_not_none(a, b):
    """
    Returns the minimum of a and b, ignoring None values. If both are None, 0
    will be returned
    """
    if a is None and b is None:
        return 0
    return min(element for element in [a, b] if element != None)


def length_of_shortest_path(matrix):
    """
    Returns the length of the shortest path through a matrix where you can only
    traverse down or right
    """
    # Use a dynamic programing approach. Start from the bottom right and
    # update each element so that they equal their value plus the minimum of
    # the element to the right or down
    for x, y in iterate_zigzag(matrix):
        right = matrix[x+1][y] if x+1 < len(matrix) else None
        down = matrix[x][y+1] if y+1 < len(matrix) else None
        matrix[x][y] += min_of_not_none(right, down)

    return matrix[0][0]


def main():
    matrix = np.loadtxt("p081_matrix.txt", dtype=int, delimiter=',')
    answer = length_of_shortest_path(matrix)
    print(answer)

if __name__ == '__main__':
  main()
