import numpy as np

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
    up = best_distances[row-1][col] if row > 0 else 99999999999999 # FIXME: HACK
    down = best_distances[row+1][col] if row < matrix.shape[0]-1 else 99999999999999 # FIXME: HACK

    # The best distances to the right and up should already be known
    best_distances[row][col] = matrix[row][col] + min(right, up, down)

def set_best_distance_no_up(row, col, best_distances, matrix):
    print("@", row, col)
    right = best_distances[row][col + 1]
    down = best_distances[row+1][col] if row < matrix.shape[0]-1 else 99999999999999 # FIXME: HACK

    best_distances[row][col] = matrix[row][col] + min(right, down)

def length_of_shortest_path(matrix):
    # 0 denotes that the best distance has not yet been computed
    best_distances = np.zeros_like(matrix)
    # best_distances = np.empty_like(matrix)
    # best_distances.fill(np.nan)

    # Set the last column's best distance to the value of the matrix
    for row in range(matrix.shape[0]):
        best_distances[row][-1] = matrix[row][-1]

    # From the second-last column to the first column
    for col in reversed(range(matrix.shape[1]-1)):
        for row in range(matrix.shape[0]):
            set_best_distance(row, col, best_distances, matrix)
            print(row, col)
            print(best_distances)
            print()
            # best_distances[row][col] = best_distance(row,
            #                                                col,
            #                                                best_distances,
            #                                                matrix)
            # best_distances[row][col] = np.nanmin([best_distance(row, # Right
            #                                                           col + 1,
            #                                                           best_distances,
            #                                                           matrix),
            #                                             best_distance(row + 1, # Down
            #                                                           col,
            #                                                           best_distances,
            #                                                           matrix),
            #                                             best_distance(row - 1, # Up
            #                                                           col,
            #                                                           best_distances,
            #                                                           matrix)])

    print(best_distances)

    # The shortest path is the minimum of the first column of best distances
    return min(best_distances[:,0])

def main():
    matrix = MATRIX
    # matrix = np.loadtxt("p083_matrix.txt", dtype=int, delimiter=',')
    answer = length_of_shortest_path(matrix)
    print(answer)

if __name__ == '__main__':
    main()