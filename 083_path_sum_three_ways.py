import numpy as np

MATRIX = np.array([[131, 673, 234, 103, 18],
                   [201, 96, 342, 965, 150],
                   [630, 803, 736, 422, 111],
                   [537, 699, 497, 121, 956],
                   [805, 732, 524, 37, 331]])

def length_of_shortest_path(matrix):
    pass

def main():
    matrix = MATRIX
    # matrix = np.loadtxt("p083_matrix.txt", dtype=int, delimiter=',')
    answer = length_of_shortest_path(matrix)
    print(answer)

if __name__ == '__main__':
    main()