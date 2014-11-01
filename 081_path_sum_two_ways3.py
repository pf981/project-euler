import numpy as np

MATRIX = np.array([[131, 673, 234, 103, 18],
                   [201, 96, 342, 965, 150],
                   [630, 803, 746, 422, 111],
                   [537, 699, 497, 121, 956],
                   [805, 732, 524, 37, 331]])

def iterate_zigzag(tree):
    """
    Iterates over the tree in the following order
    17 15 13 10
    14 12 9  6
    11 8  5  3
    7  4  2  1
    """
    # In the docstring example, this iterates through 1 to 10
    for start_column in reversed(range(len(tree))):
        for row in reversed(range(start_column + 1, len(tree))):
            yield (row, len(tree) + start_column - row)

    # In the docstring example, this iterates through 11 to 17
    for start_row in reversed(range(len(tree))):
        for column in range(start_row + 1):
            yield (start_row - column, column)


def min_of_not_none(a, b):
    if a is None and b is None:
        return 0
    return min(element for element in [a, b] if element != None)


def length_of_shortest_path(tree):
    """
    Returns the length of the shortest path through a tree where you can only
    traverse down or right
    """
    # Use a dynamic programing approach. Start from the bottom right and
    # update each element so that they equal their value plus the minimum of
    # the element to the right or down
    for x, y in iterate_zigzag(tree):
        right = tree[x+1][y] if x+1 < len(tree) else None
        down = tree[x][y+1] if y+1 < len(tree) else None
        tree[x][y] += min_of_not_none(right, down)

    return tree[0][0]


def main():
    matrix = np.loadtxt("p081_matrix.txt", dtype=int, delimiter=',')
    answer = length_of_shortest_path(matrix)
    print(answer)

if __name__ == '__main__':
  main()
