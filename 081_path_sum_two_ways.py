import numpy as np

MATRIX = np.array([[131, 673, 234, 103, 18],
                   [201, 96, 342, 965, 150],
                   [630, 803, 736, 422, 111],
                   [537, 699, 497, 121, 956],
                   [805, 732, 524, 37, 331]])

def main():
    # print(MATRIX)

    diags = [MATRIX[::-1,:].diagonal(i) for i in range(-MATRIX.shape[0]+1,MATRIX.shape[1])]
    # diags = [MATRIX.diagonal(i) for i in range(-MATRIX.shape[0]+1,MATRIX.shape[1])]

# Now back to the original array to get the upper-left-to-lower-right diagonals,
# starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
    # diags.extend(MATRIX.diagonal(i) for i in range(MATRIX.shape[1]-1,-MATRIX.shape[0],-1))

    # print(diags)

    for row in diags:
        print(row)

    # for row in reversed(len(MATRIX) - 1):
    #     for col in range(len(MATRIX[row])):
    #         MARTIX[row][col] += max(tree[row + 1][col], tree[row + 1][col + 1])

    # FOR EACH / DIAGONAL
    #    UPDATE IT
    #        THe bottom right corner is the answer!

    answer = 0
    print(answer)

if __name__ == '__main__':
  main()
