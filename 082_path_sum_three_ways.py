import numpy as np
from helpers import lists

# This is just for testing if this solution works against the example. The
# actual matrix is read in from a file
MATRIX = np.array([[131, 673, 234, 103, 18],
                   [201, 96, 342, 965, 150],
                   [630, 803, 736, 422, 111],
                   [537, 699, 497, 121, 956],
                   [805, 732, 524, 37, 331]])

def set_best_distance(row, col, best_distances, matrix):
    # Compute the cells down
    for down_row in reversed(range(row+1, matrix.shape[0])):
        set_best_distance_no_up(down_row, col, best_distances, matrix)

    right = best_distances[row][col + 1]
    up = best_distances[row-1][col] if row > 0 else None
    down = best_distances[row+1][col] if row < matrix.shape[0]-1 else None

    # The best distances to the right and up should already be known
    best_distances[row][col] = matrix[row][col] + lists.min_of_not_none(right, up, down)

def set_best_distance_no_up(row, col, best_distances, matrix):
    right = best_distances[row][col + 1]
    down = best_distances[row+1][col] if row < matrix.shape[0]-1 else None

    best_distances[row][col] = matrix[row][col] + lists.min_of_not_none(right, down)

def length_of_shortest_path(matrix):
    # best_distances[row][col] is an integer that denotes the minimum distance
    # from (row, col) to the far right column. The minimum path will just be
    # the smallest value in the left-most column of best_distances
    best_distances = np.empty_like(matrix)

    # Set the last column's best distance to the value of the matrix
    for row in range(matrix.shape[0]):
        best_distances[row][-1] = matrix[row][-1]

    # From the second-last column to the first column
    for col in reversed(range(matrix.shape[1]-1)):
        # From the first row to the last row
        for row in range(matrix.shape[0]):
            # Determine the length of the minimal path from (row, col) to the
            # far right column
            set_best_distance(row, col, best_distances, matrix)

    # The shortest path is the minimum of the first column
    return min(best_distances[:,0])

def main():
    # matrix = MATRIX
    matrix = np.loadtxt("p082_matrix.txt", dtype=int, delimiter=',')
    answer = length_of_shortest_path(matrix)
    print(answer)

if __name__ == '__main__':
    main()