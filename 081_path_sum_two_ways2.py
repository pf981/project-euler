import sys
import numpy as np

MATRIX = np.array([[131, 673, 234, 103, 18],
                   [201, 96, 342, 965, 150],
                   [630, 803, 736, 422, 111],
                   [537, 699, 497, 121, 956],
                   [805, 732, 524, 37, 331]])

def iterate_zigzag(tree):
    """
    Iterates over the tree in the following order
    1  3  6  9
    2  5  8  11
    4  7  10 12
    """
    print(tree[0][0])
    print()
    for start_row in range(len(tree)):
        for column in range(start_row + 1):
            print(start_row, column, tree[start_row - column][column])
    print()
    for start_column in range(len(tree)):
        for row in reversed(range(start_column + 1, len(tree))):
            print(start_column, row, tree[row][start_column - row])


    return [(1, 2), (1, 2)]

def min_of_not_none(a, b):
    return min(element for element in [a, b] if element != None)

# This is the same code as 018
def length_of_shortest_path(tree):
    """
    Returns the length of the shortest path through a tree where you can only
    traverse down or right
    """
    for x, y in iterate_zigzag(tree):
        tree[x][y] += min_of_not_none(
            tree[x+1][y], # Right
            tree[x][y+1]) # Down

    return tree[0][0]


def main():
    answer = length_of_shortest_path(MATRIX)
    print(answer)

if __name__ == '__main__':
  main()
